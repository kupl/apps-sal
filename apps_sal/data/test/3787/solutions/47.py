import sys
input = sys.stdin.readline
N, A, B = map(int, input().split())
if N < A or N < B:
    print(-1)
    return
res = [x for x in range(N - A + 1, N + 1)]
k = N - A
if k < B - 1:
    print(-1)
    return
b = [0] * (B - 1)
for i in range(k):
    b[i % (B - 1)] += 1
if len(b):
    if max(b) > A:
        print(-1)
        return
for i in b:
    t = [x for x in range(k - i + 1, k + 1)]
    res += t
    k -= i
print(*res)
