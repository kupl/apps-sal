a, b = map(int, input().split())

ans = []
ans.append(a)
ans.append(b)
ans = sorted(ans)

anser = ''
for i in range(ans[1]):
    anser += str(ans[0])

print(anser)
