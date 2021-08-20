n = [int(i) for i in input().split()]
a = str(input())
for i in range(n[1]):
    a += '0'
d = n[1]
skak = 0
pr = d
ans = 0
while skak < n[0] - 1 and pr > 0:
    pr = d
    while a[pr + skak] != '1' and pr != 0:
        pr -= 1
    skak = pr + skak
    ans += 1
if pr == 0:
    print(-1)
else:
    print(ans)
