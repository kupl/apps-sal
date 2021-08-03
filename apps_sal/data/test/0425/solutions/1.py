def get_n(bin_n):
    ans = 0
    while bin_n > 0:
        ans += bin_n & 1
        bin_n >>= 1
    return ans


n, p = map(int, input().split())
ans = 1
while ans < 10 ** 5 * 2 and not (n - p * ans >= ans >= get_n(n - p * ans)):
    ans += 1
if ans == 10 ** 5 * 2:
    print(-1)
else:
    print(ans)
