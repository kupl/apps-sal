(n, t) = list(map(int, input().split()))
mn = 1001
for i in range(n):
    (c, tn) = list(map(int, input().split()))
    if tn <= t and c < mn:
        mn = c
if mn == 1001:
    print('TLE')
else:
    print(mn)
