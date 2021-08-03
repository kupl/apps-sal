a = dict()
for i in range(int(input()) - 1):
    c = int(input())
    if (not c in a):
        a[c] = list()
    a[c].append(i + 2)
for i in a:
    l = int()
    for j in a[i]:
        if (j not in a):
            l += 1
    if (l < 3):
        print("No")
        return
print("Yes")
