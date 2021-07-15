n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7
ans = 0

for i in range(60):
    cnt = 0
    digit = 1 << i
    for j in a:
        if digit & j:
            cnt += 1
    ans += digit*cnt*(n - cnt)%mod

print(ans%mod)
