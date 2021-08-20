(n, p) = list(map(int, input().split()))
s = input()
res = 0
if p == 2 or p == 5:
    for i in range(n):
        if int(s[i]) % p == 0:
            res += i + 1
else:
    s = s[::-1]
    cnt = {0: 1}
    now = 0
    d = 1
    for i in range(n):
        now = (now + int(s[i]) * d) % p
        res += cnt.get(now, 0)
        d = d * 10 % p
        cnt[now] = cnt.get(now, 0) + 1
print(res)
