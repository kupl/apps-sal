(n, k) = map(int, input().split())
ans = 0


def f(y):
    if 1 <= y <= n + 1:
        return y - 1
    else:
        return 2 * (n + 1) - y - 1


for A in range(2, 2 * n + 1):
    B = A - k
    if 2 <= B <= 2 * n:
        ans += f(A) * f(B)
print(ans)
