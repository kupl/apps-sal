a = int(input())
d = input()
s = 0
f = 0
now = d[0]
for i in range(1, a):
    if d[i] == "S":
        if now != d[i]:
            now = d[i]
            f += 1
    else:
        if now != d[i]:
            now = d[i]
            s += 1
    now = d[i]
if s > f:
    print("YES")
else:
    print("NO")
