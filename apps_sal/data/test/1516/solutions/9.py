n = int(input())
ans = 0
mod = 998244353
li = input().split()
for i in li:
    t = 10
    for j in i[::-1]:
        ans += (ord(j) - ord('0')) * t * n
        ans += (ord(j) - ord('0')) * (t // 10) * n
        t *= 100
    ans %= mod
print(ans)

