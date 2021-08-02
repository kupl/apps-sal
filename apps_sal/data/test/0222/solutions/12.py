n = input()
ps = []
for i in range(44722):
    ps.append(str(i * i))
ans = 20
for i in range(1, 44722):
    k = 0
    l = len(ps[i])
    for j in n:
        if j == ps[i][k]:
            k += 1
        if k == l:
            break
    if k == l:
        ans = min(ans, len(n) - l)
if ans == 20:
    ans = -1
print(ans)
