import heapq,bisect

def main():
    n,m = map(int,input().split())
    trees = list(map(int,input().split()))
    trees.sort()

    ans = []
    distance = 0
    heap = []
    visited = set()
    for i in trees:
        visited.add(i)

    for i in trees:
        if i+1 not in visited:
            heapq.heappush(heap,(1,i+1))
        if i-1 not in visited:
            heapq.heappush(heap,(1,i-1))

    while heap:
        curr = heapq.heappop(heap)
        if curr[1] not in visited:
            distance += curr[0]
            ans.append(curr[1])
            visited.add(curr[1])
            if len(ans) == m:
                break

            if curr[1]+1 not in visited:
                index = bisect.bisect(trees,curr[1]+1)
                min_dist = float('inf')
                if index < len(trees):
                    min_dist = min(min_dist,trees[index]-curr[1]-1)
                if index-1 >= 0:
                    min_dist = min(min_dist,curr[1]+1-trees[index-1])

                heapq.heappush(heap,(min_dist,curr[1]+1))

            if curr[1]-1 not in visited:
                index = bisect.bisect(trees,curr[1]-1)
                min_dist = float('inf')
                if index < len(trees):
                    min_dist = min(min_dist,trees[index]-curr[1]+1)
                if index-1 >= 0:
                    min_dist = min(min_dist,curr[1]-1-trees[index-1])

                heapq.heappush(heap,(min_dist,curr[1]-1))
        


    print(distance)
    for i in ans:
        print(i,end = ' ')


main()

