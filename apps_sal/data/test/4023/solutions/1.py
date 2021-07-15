n = int(input())
a = list(map(int, input().split()))
b = [[a[0], 1]]
fl = False
for i in range(1, n):
    if fl:
        break
    if a[i] == b[-1][0]:
        b[-1][1] += 1
    elif a[i] < b[-1][0]:
        b.append([a[i], 1])
    else:
        while len(b) != 0 and a[i] > b[-1][0]:
            if b[-1][1] % 2 != 0:
                print("NO")
                fl = True
                break
            b.pop()
        if len(b) == 0 or a[i] < b[-1][0]:
            b.append([a[i], 1])
        else:
            b[-1][1] += 1
if not fl:
    i = len(b) - 1
    while i != 0:
        if b[i][1] % 2 != 0:
            fl = True
            break
        i -= 1
    if fl:
        print("NO")
    else:
        print("YES")
                             

