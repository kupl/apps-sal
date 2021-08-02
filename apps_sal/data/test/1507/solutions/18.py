from collections import defaultdict as dd

# milanmilanmilan
a, k = [int(i) for i in input().split()]
b = input()
al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
come = [0] * (26)
out = [0] * (26)
for i in range(a):
    if come[al.index(b[i])] == 0:
        come[al.index(b[i])] = i + 1
        out[al.index(b[i])] = i + 1
    else:
        out[al.index(b[i])] = i + 1
cm = []
for i in range(26):
    if come[i] != 0 and out[i] != 0:
        cm.append((come[i], 1))
        cm.append((out[i], 2))
cm.sort()
ma = 0
ans = 0
for i in cm:
    if i[1] == 1:
        ma += 1
    else:
        ma -= 1
    ans = max(ma, ans)
if (k >= ans):
    print("NO")
else:
    print("YES")
