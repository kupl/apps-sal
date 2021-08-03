n, p = list(map(int, input().split()))
s = list(map(int, list(input())))[::-1]

sum = 0
cnt = [0] * p
cnt[0] = 1
n = len(s)
for i in range(n):
    d = s[i] * pow(10, i, p)
    sum = (sum + d) % p
    cnt[sum] += 1

ans = 0
if p in [2, 5]:
    if p == 2:
        ok_list = [0, 2, 4, 6, 8]
    if p == 5:
        ok_list = [0, 5]

    for i in range(n):
        d = s[i]
        if d in ok_list:
            ans += n - i

else:
    for i in range(p):
        ans += cnt[i] * (cnt[i] - 1) // 2


print(ans)
