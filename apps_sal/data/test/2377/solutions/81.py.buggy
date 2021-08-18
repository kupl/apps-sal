n, h = map(int, input().split())
abl = [list(map(int, input().split())) for nesya in range(n)]
abl.sort()
amax = abl[-1][0]
b_list = []
for ab in abl:
    b = ab[1]
    if amax <= b:
        b_list.append(b)
b_list.sort()
ans = 0
for num in b_list[::-1]:
    h -= num
    ans += 1
    if h <= 0:
        print(ans)
        return
if h % amax == 0:
    print(ans + h // amax)
else:
    print(ans + h // amax + 1)
