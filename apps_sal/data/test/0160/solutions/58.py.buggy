import heapq
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

x = sum(a)
search = []
i = 1
while i ** 2 <= x:
    if x % i == 0:
        heapq.heappush(search, -i)
        heapq.heappush(search, -x // i)
    i += 1

while search:
    ans = -heapq.heappop(search)
    u = [a[i] % ans for i in range(n)]
    u.sort()

    plus = [0]
    minus = [0]
    for i in range(n):
        plus.append(plus[-1] + ans - u[i])
        minus.append(minus[-1] + u[i])

    for i in reversed(list(range(n + 1))):
        # print(i)
        m = minus[i]
        p = plus[-1] - plus[i]
        if m == p and m <= k:
            print(ans)
            return
