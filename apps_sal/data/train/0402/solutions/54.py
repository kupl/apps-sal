import heapq

def solve(b,s,t):
    def create_priority_item(c, t):
        dx = c[0]-t[0]
        dy = c[1]-t[1]
        d2 = dx*dx + dy*dy
        return (d2, c)

    b = set(tuple(_b) for _b in b)
    s = tuple(s)
    t = tuple(t)
    heap = [(-1,s)]
    visited = set()
    iter = -1
    while heap:
        iter += 1
        if iter > 1.1e5:
            return False
        _, c = heapq.heappop(heap)
        if c in visited or c in b or c[0] < 0 or c[0] >=1e6 or c[1]<0 or c[1]>=1e6:
            continue
        if c == t:
            # found!
            return True
        # search neighbors:
        dx = c[0] - s[0]
        dy = c[1] - s[1]
        if dx*dx + dy*dy > 201*201:
            print(('found!', c, t))
            return True

        visited.add(c)
        # x = c[0]
        # while t[0] > x and (x+1,c[1]) not in b:
        #     x += 1
#         heapq.heappush(heap, create_priority_item((x, c[1]  ), t))
#         x = c[0]
#         while t[0] < x and (x-1,c[1]) not in b:
#             x -= 1
#         heapq.heappush(heap, create_priority_item((x, c[1]  ), t))

#         y = c[1]
#         while t[1] > y and (c[0],y+1) not in b:
#             y += 1
#         heapq.heappush(heap, create_priority_item((c[0], y  ), t))
#         y = c[1]
#         while t[1] < y and (c[0],y-1) not in b:
#             y -= 1
#         heapq.heappush(heap, create_priority_item((c[0], y  ), t))


        heapq.heappush(heap, create_priority_item((c[0]+1, c[1]  ), t))
        heapq.heappush(heap, create_priority_item((c[0]-1, c[1]  ), t))
        heapq.heappush(heap, create_priority_item((c[0]  , c[1]+1), t))
        heapq.heappush(heap, create_priority_item((c[0]  , c[1]-1), t))
    # we live in a cavity :(
    return False

def solve_both(b,s,t):
    return solve(b,s,t) and solve(b,t,s)




class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        return solve_both(blocked, source, target)

