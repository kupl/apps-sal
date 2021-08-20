N = int(input())
mod = 10 ** 9 + 7
ans = 1
for i in range(N):
    ans = ans * (i + 1) % mod
print(ans)
