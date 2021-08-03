n = int(input())

d = {}

for _ in range(n):
    t = int(input())
    if t not in d:
        d[t] = 0
    d[t] += 1

if len(d) != 2:
    print("NO")
    return

k = list(d.keys())

if d[k[0]] != d[k[1]]:
    print("NO")
else:
    print("YES")
    print(str(k[0]) + " " + str(k[1]))
