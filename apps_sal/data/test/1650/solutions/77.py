l = input()
ans = 1
cnt = 1
mod = 10 ** 9 + 7
for i in l[::-1]:
    if i == '1':
        ans *= 2
        ans += cnt
        ans %= mod
    cnt *= 3
    cnt %= mod
print(ans)
