n = int(input())
hs = list(map(int, input().split()))

maxx = 0
ans = []
for h in reversed(hs):
    if h > maxx:
        ans.append(0)
    else:
        ans.append(maxx - h + 1)
    maxx = max(maxx, h)

print(' '.join(map(str, reversed(ans))))
