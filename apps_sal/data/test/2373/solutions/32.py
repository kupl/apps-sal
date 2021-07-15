N = int(input())
P = list(map(int, input().split()))

t = []
for i, p in enumerate(P):
    if (i + 1) == p:
        t.append(i)

ans = 0
checked = [False] * len(t)
for i in range(len(t)):
    if checked[i]:
        continue
    if i + 1 < len(t) and t[i] + 1 == t[i + 1]:
        checked[i] = True
        checked[i + 1] = True
    else:
        checked[i] = True
    ans += 1
print(ans)


