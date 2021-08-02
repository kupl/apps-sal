def rotate(L):
    L1 = ['' for i in range(n)]
    for i in range(n):
        for j in range(n):
            L1[n - j - 1] += L[i][j]
    return L1


def flip_v(L):
    L1 = []
    for i in range(n):
        L1.append(L[i][::-1])
    return L1


def flip_h(L):
    L1 = []
    for i in range(n):
        L1.append(L[n - i - 1])
    return L1


n = int(input())
L = []
M = []
for i in range(n):
    L.append(input())
for i in range(n):
    M.append(input())
L1 = rotate(L)
L2 = rotate(L1)
L3 = rotate(L2)
L4 = flip_v(L)
L5 = flip_h(L)
L6 = rotate(L4)
L7 = rotate(L6)
L8 = rotate(L7)
L9 = rotate(L5)
L10 = rotate(L9)
L11 = rotate(L10)
if L == M or L1 == M or L2 == M or L3 == M or L4 == M or L5 == M or L6 == M or L7 == M or L8 == M or L9 == M or L10 == M or L11 == M:
    print('Yes')
else:
    print('No')
