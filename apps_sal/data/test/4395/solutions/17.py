n = int(input())
s = input()
best = -1
ans = 10 ** 6
per = ['RGB', 'RBG', 'BRG', 'BGR', 'GBR', 'GRB']
for (idx, p) in enumerate(per):
    tmp = 0
    for i in range(n):
        if s[i] != p[i % 3]:
            tmp += 1
    if tmp < ans:
        ans = tmp
        best = idx
out = per[best] * (n // 3) + per[best][:n % 3]
print(ans)
print(out)
