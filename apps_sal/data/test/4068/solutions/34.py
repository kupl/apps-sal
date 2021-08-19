(n, m) = map(int, input().split())
a = set([int(input()) for _ in range(m)])
mod = 10 ** 9 + 7
ans = [0] * (n + 1)
ans[0] = 1
if 1 not in a:
    ans[1] = 1
for i in range(2, n + 1):
    if i in a:
        continue
    ans[i] = ans[i - 1] + ans[i - 2]
print(ans[-1] % mod)
