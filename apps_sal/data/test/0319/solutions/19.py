n, m = map(int, input().split())
r = [input() for _ in [0] * n]
d = {j: 0 for j in range(m)}
for i in r:
    for j in range(m):
        d[j] += int(i[j])
l = list(d.values())
for i in r:
    f = True
    for j in range(m):
        if i[j] == '1' and l[j] == 1:
            f = False
            break
    if f:
        print("YES")
        return
print("NO")
