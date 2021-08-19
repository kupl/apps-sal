input()
d = {}
for i in map(int, input().split()):
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
d = dict(sorted(d.items(), reverse=True))
ans = []
for (i, j) in d.items():
    if len(ans) < 2 and j >= 4:
        ans.append(i)
        d[i] -= 2
    if len(ans) < 2 and j >= 2:
        ans.append(i)
        d[i] -= 2
    if len(ans) == 2:
        print(ans[0] * ans[1])
        break
else:
    print(0)
