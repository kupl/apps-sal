s = list(input())
x, y = map(int, input().split())
P = "A"
A = []
X = [0]
Y = [0]

cnt = 0
for i in range(len(s)):
    if P == "A":
        if s[i] == "F":
            cnt += 1
        else:
            A.append(cnt)
            cnt = 0
            P = "Y"
    elif P == "X":
        if s[i] == "F":
            cnt += 1
        else:
            X.append(cnt)
            cnt = 0
            P = "Y"
    else:
        if s[i] == "F":
            cnt += 1
        else:
            Y.append(cnt)
            cnt = 0
            P = "X"
if P == "A":
    A.append(cnt)
elif P == "X":
    X.append(cnt)
else:
    Y.append(cnt)

DX1 = {}
DX1[0] = 1
DX2 = {}
for i in X:
    for j in DX1:
        DX2[j + i] = 1
        DX2[j - i] = 1
    DX1 = DX2
    DX2 = {}
if x - A[0] in DX1:
    flagx = 1
else:
    flagx = 0

DY1 = {}
DY1[0] = 1
DY2 = {}
for i in Y:
    for j in DY1:
        DY2[j + i] = 1
        DY2[j - i] = 1
    DY1 = DY2
    DY2 = {}
if y in DY1:
    flagy = 1
else:
    flagy = 0

if flagx * flagy == 1:
    print("Yes")
else:
    print("No")
