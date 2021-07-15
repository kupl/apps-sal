import heapq

n, m = map(int,input().split())
ab = [[0] * 2 for i in range(n)]
for i in range(n):
    a, b = map(int,input().split())
    ab[i][0], ab[i][1] = a, -1*b
heapq.heapify(ab)

b = [0]
heapq.heapify(b)
ans = 0
for i in range(1, m+1):
    while ab:
        tmp = heapq.heappop(ab)
        if tmp[0] <= i:
            heapq.heappush(b, tmp[1])    
        else:
            heapq.heappush(ab, tmp)
            break
    if b:
        ans -= heapq.heappop(b)
print(ans)
