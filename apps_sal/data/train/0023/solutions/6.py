import heapq
 
for _ in range(int(input())):
    n = int(input())
    voters = []
    for i in range(n):
        m,p = list(map(int, input().split()))
        voters.append((m, -p))
    voters.sort()
    for i in range(n):
        voters[i] = (voters[i][0], -voters[i][1])
 
    ans = 0
    costs = []
    heapq.heapify(costs)
    bought = 0
    for i in range(n-1, -1, -1):
        buysNeeded = voters[i][0] - i  - bought
        heapq.heappush(costs, voters[i][1])
        while buysNeeded > 0 and len(costs) > 0:
            ans += heapq.heappop(costs)
            bought += 1
            buysNeeded -= 1
 
    print(ans)
