x, y, l, r = list(map(int, input().split()))
lx = []
ly = []
for i in range(65):
    if x**i > r:
        break
    lx.append(x**i)
for i in range(65):
    if y**i > r:
        break
    ly.append(y**i)

ans = set()
for i in lx:
    for j in ly:
        if l <= i + j <= r:
            ans.add(i + j)

ans.add(l - 1)
ans.add(r + 1)
ans = sorted(list(ans))
anslen = 0
for i in range(1, len(ans)):
    anslen = max(anslen, ans[i] - ans[i - 1] - 1)

# print(ans)
print(anslen)
