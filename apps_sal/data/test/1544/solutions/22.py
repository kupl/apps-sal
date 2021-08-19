import math
f = math.factorial


def C(n, k):
    if k > n:
        return 1
    return f(n) // f(k) // f(n - k)


n = int(input())
ans1 = C(n, 1)
if n > 1:
    ans1 += 2 * C(n, 2)
if n > 2:
    ans1 += C(n, 3)
ans2 = C(n, 1)
if n > 1:
    ans2 += 4 * C(n, 2)
if n > 2:
    ans2 += 6 * C(n, 3)
if n > 3:
    ans2 += 4 * C(n, 4)
if n > 4:
    ans2 += C(n, 5)
print(ans1 * ans2)
