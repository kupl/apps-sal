(n, m) = map(int, input().split())
mn1 = 10
b = [False] * 9
for i in input().split():
    mn1 = min(mn1, int(i))
    b[int(i) - 1] = True
mn2 = 10
mnans = 10
for i in input().split():
    mn2 = min(mn2, int(i))
    if b[int(i) - 1]:
        mnans = min(mnans, int(i) - 1)
if mnans < 10:
    print(mnans + 1)
else:
    print(min(mn1, mn2), max(mn1, mn2), sep='')
