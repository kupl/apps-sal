class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        def bfs(s,t,b):
            q,v=[s],{s}
            while len(q)>0:
                i,j=q.pop(0)
                if (i,j)==t:return True
                if i in (s[0]+210,s[0]-210) or j in (s[1]+210,s[1]-210):return True
                for d,e in ((i+1,j),(i,j+1),(i-1,j),(i,j-1)):
                    if d>=0 and d<10**6 and e>=0 and e<10**6 and (d,e) not in v and (d,e) not in b:
                        v.add((d,e))
                        q.append((d,e))
            return False
        
        b=set(tuple(i) for i in blocked)
        return bfs(tuple(source),tuple(target),b) and bfs(tuple(target),tuple(source),b)
        
        # blocked_map = collections.defaultdict(set)
        # for r,c in blocked:
        #     blocked_map[r].add(c)
        # queue_s = collections.deque()
        # queue_s.append(source)
        # visited_s = set()
        # visited_s.add(tuple(source))
        # queue_t = collections.deque()
        # queue_t.append(target)
        # visited_t = set()
        # visited_t.add(tuple(target))
        # while queue_s and queue_t:
        #     curr = queue_s.popleft()
        #     if curr==target or tuple(curr) in visited_t:
        #         return True
        #     for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
        #         nei_r = curr[0]+dr
        #         nei_c = curr[1]+dc
        #         if nei_r>=0 and nei_r<10**6 and nei_c>=0 and nei_c<10**6:
        #             if nei_r not in blocked_map or (nei_r in blocked_map and nei_c not in blocked_map[nei_r]):
        #                 if tuple([nei_r,nei_c]) not in visited_s:
        #                     visited_s.add(tuple([nei_r,nei_c]))
        #                     queue_s.append([nei_r,nei_c])
        #     curr = queue_t.popleft()
        #     if curr == source or tuple(curr) in visited_s:
        #         return True
        #     for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
        #         nei_r = curr[0]+dr
        #         nei_c = curr[1]+dc
        #         if nei_r>=0 and nei_r<10**6 and nei_c>=0 and nei_c<10**6:
        #             if nei_r not in blocked_map or (nei_r in blocked_map and nei_c not in blocked_map[nei_r]):
        #                 if tuple([nei_r,nei_c]) not in visited_t:
        #                     visited_t.add(tuple([nei_r,nei_c]))
        #                     queue_t.append([nei_r,nei_c])
        # return False

