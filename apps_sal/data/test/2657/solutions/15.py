n = int(input())
a = list(map(int, input().split()))

a.sort()

ans_n = a[-1]
del a[-1]
ans_r = a[0]

dif = 1001001000
for i in range(n-1):
    if dif > abs(ans_n / 2 - a[i]):
        ans_r = a[i]
        dif = abs(ans_n / 2 - a[i])

print('%d %d' % (ans_n, ans_r))
