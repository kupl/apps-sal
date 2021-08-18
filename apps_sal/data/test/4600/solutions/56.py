n, m = map(int, input().split())
a = [input().split() for i in range(m)]
wa = [0] * n
ac = [0] * n

for i in range(m):
    if a[i][1] == 'AC':
        ac[int(a[i][0]) - 1] = 1
    else:
        if ac[int(a[i][0]) - 1] == 0:
            wa[int(a[i][0]) - 1] += 1
cnt1, cnt2 = 0, 0
for i in range(n):
    if ac[i] == 1:
        cnt1 += ac[i]
        cnt2 += wa[i]

print(cnt1, cnt2)
