N = int(input())
S = list(input())

a = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
ans = ''
for s in S:
    num = a.index(s) + N
    if num <= 25:
        ans += a[num]
    else:
        ans += a[num - 26]

print(ans)
