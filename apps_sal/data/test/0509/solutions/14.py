import sys
n = int(input())
tab = [0]
for i in range(n):
    newtab = []
    new = int(input())
    for j in tab:
        newtab.append(j + new)
        newtab.append(j - new)
    tab = newtab
for i in tab:
    if i % 360 == 0:
        print("YES")
        return
print("NO")
