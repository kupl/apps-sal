n, m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))
mod = 10**9 + 7
ans = 0


def sum_S(a, z):
    ans = 0
    for i in range(len(z)):
        z_i = z[i] * (2 * i + 1 - a)
        ans += z_i
    return ans


ans_x = sum_S(n, x)
ans_y = sum_S(m, y)
res = (ans_x * ans_y) % mod
print(res)
