(n, p) = [int(i) for i in input().split()]
s = [int(i) for i in list(input())][::-1]
summ = 0
ans = 0
cnt = [0] * p
cnt[0] = 1
for i in range(n):
    d = s[i] * pow(10, i, p)
    summ = (summ + d) % p
    cnt[summ] += 1
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
