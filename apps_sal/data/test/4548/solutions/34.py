n, m, x = list(map(int, input().split()))
a = list(map(int, input().split()))
cnt1 = 0
cnt2 = 0
x1 = x
x2 = x

while x1 < n+1:
    x1 += 1
    if x1 in a:
        cnt1 += 1

while x2 > 0:
    x2 -= 1
    if x2 in a:
        cnt2 += 1



if cnt1 < cnt2:
    ans = cnt1
else:
    ans = cnt2

print(ans)

