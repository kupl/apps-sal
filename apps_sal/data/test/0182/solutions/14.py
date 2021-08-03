def f(x):
    return x if x <= 0 else x // 2


(a, b, c) = list(map(int, input().split()))
(x, y, z) = list(map(int, input().split()))
(n, m, k) = (a - x, b - y, c - z)
ans = f(n) + f(m) + f(k)
if ans >= 0:
    print("Yes")
else:
    print("No")
