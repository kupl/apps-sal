n = int(input())
s = 0
ms = []
o = 1
z = 0
q = 0
for _ in range(n):
    a = list(map(int, input().split()))
    if a[0] == 1:
        s = a[1]
        while len(ms) > 0 and ms[-1] < s:
            z += 1
            ms.pop(-1)
    elif a[0] == 2:
        if o != 1:
            z += 1 - o
            o = 1
    elif a[0] == 3:
        ms.append(a[1])
        while len(ms) > 0 and ms[-1] < s:
            z += 1
            ms.pop(-1)
    elif a[0] == 4:
        o = 1
    elif a[0] == 5:
        ms = []
    elif a[0] == 6:
        o -= 1
print(z)
