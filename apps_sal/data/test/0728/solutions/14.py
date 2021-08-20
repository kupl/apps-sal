import heapq
n = int(input())
a = list(map(int, input().split()))
b = a[0]
a = a[1:]
for i in range(n - 1):
    a[i] = -a[i]
heapq.heapify(a)
ans = 0
while True:
    cur = heapq.heappop(a)
    cur = -cur
    if cur < b:
        break
    ans += 1
    b += 1
    cur -= 1
    cur = -cur
    heapq.heappush(a, cur)
print(ans)
