ans = 0
curheight = 0
n = int(input())

for i in range(n):
    x = int(input())
    if i > 0:
        ans += 1

    if x > curheight:
        ans += (1 + x - curheight)
    else:
        ans += (1 + curheight - x)
    curheight = x

print(ans)
