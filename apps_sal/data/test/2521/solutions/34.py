from heapq import heapify, heappushpop
n = int(input())
a = list(map(int, input().split()))
a1 = a[:n]
heapify(a1)
a2 = a[n:2 * n]
a3 = [-i for i in a[2 * n:]]
heapify(a3)
b1 = [sum(a1)]
b2 = [sum(a3)]
for i in range(n):
    b1.append(b1[-1] + a2[i] - heappushpop(a1, a2[i]))
    b2.append(b2[-1] - heappushpop(a3, -a2[n - i - 1]) - a2[n - i - 1])
ans = b1[0] + b2[n]
for i in range(n + 1):
    ans = max(ans, b1[i] + b2[n - i])
print(ans)
