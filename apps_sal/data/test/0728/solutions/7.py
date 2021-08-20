import heapq
n = int(input())
votes = [-int(e) for e in input().split()]
limak = -votes[0]
votes = votes[1:]
heapq.heapify(votes)
ans = 0
while limak <= -votes[0]:
    cur = heapq.heappop(votes)
    cur += 1
    limak += 1
    ans += 1
    heapq.heappush(votes, cur)
print(ans)
