(n, l) = map(int, input().split())
isMina = False
isPlu = False
ans = []
for i in range(1, n + 1):
    ans.append(l + i - 1)
    if l + i - 1 < 0:
        isMina = True
    elif i + i - 1 > 0:
        isPlu = True
print(sum(ans) - min(ans) if not isMina else sum(ans) - max(ans) if not isPlu else sum(ans))
