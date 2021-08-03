a = [[int(i) for i in input().split()] for j in range(4)]

pesh = [0] * 4
avt = [0] * 4

for i in range(len(a)):
    if a[i][3]:
        pesh[i] = True
    if a[i][0]:
        avt[(i - 1) % 4] = True
        avt[i] = True
    if a[i][1]:
        avt[(i + 2) % 4] = True
        avt[i] = True
    if a[i][2]:
        avt[(i + 1) % 4] = True
        avt[i] = True

for i in range(4):
    if avt[i] and pesh[i]:
        print("YES")
        break
else:
    print("NO")
