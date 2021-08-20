import heapq
n = int(input())
a = list(map(int, input().split()))
s1 = sum(a[:n])
hq1 = a[:n]
heapq.heapify(hq1)
A = [s1]
for i in range(n, 2 * n):
    s1 += a[i]
    heapq.heappush(hq1, a[i])
    x = heapq.heappop(hq1)
    s1 -= x
    A.append(s1)
a = a[::-1]
s2 = sum(a[:n])
hq2 = [-a[i] for i in range(n)]
heapq.heapify(hq2)
B = [s2]
for i in range(n, 2 * n):
    s2 += a[i]
    heapq.heappush(hq2, -a[i])
    x = heapq.heappop(hq2)
    s2 -= -x
    B.append(s2)
B = B[::-1]
ans = -10 ** 18
for i in range(len(A)):
    ans = max(ans, A[i] - B[i])
print(ans)
