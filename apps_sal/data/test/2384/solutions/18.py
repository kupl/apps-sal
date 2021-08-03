from itertools import accumulate
n = int(input())
A = list(map(int, input().split()))
L = [0]
R = []
min_L = float("inf")
for i, a in enumerate(A):
    b = A[-(i + 1)]
    if i % 2 == 0:
        L.append(a)
    else:
        R.append(a)
R.append(0)
L = list(accumulate(L))
R = list(accumulate(R[::-1]))[::-1]
ans = -float("inf")
if n % 2:
    def f(A):
        temp = 0
        left = 0
        right = 0
        for i in range(2, n, 2):
            temp += A[i]
        res = max(ans, temp)
        for i in range(1, n // 2):
            temp -= A[i * 2]
            left, right = left + A[2 * (i - 1)], max(left, right) + A[2 * (i - 1) + 1]
            res = max(res, temp + max(left, right))
        return res
    ans = max(f(A), f(A[::-1]))
    temp = 0
    for i in range(1, n, 2):
        temp += A[i]
    ans = max(ans, temp)
else:
    for l, r in zip(L, R):
        ans = max(ans, l + r)
print(ans)
