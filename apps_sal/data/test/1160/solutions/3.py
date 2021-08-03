# You lost the game.
import sys
T = list(map(int, input().split()))
L = [[] for _ in range(6)]
D = [[] for _ in range(5)]
n = int(input())
S = [str(input()) for _ in range(n)]
for i in range(n):
    x = list(S[i].split(","))
    if len(x) == 2:
        if x[0] == "S":
            D[0] += [i]
        if x[0] == "M":
            D[1] += [i]
        if x[0] == "L":
            D[2] += [i]
        if x[0] == "XL":
            D[3] += [i]
        if x[0] == "XXL":
            D[4] += [i]
        if x[0] == "XXXL":
            D[5] += [i]
    else:
        if x[0] == "S":
            L[0] += [i]
        if x[0] == "M":
            L[1] += [i]
        if x[0] == "L":
            L[2] += [i]
        if x[0] == "XL":
            L[3] += [i]
        if x[0] == "XXL":
            L[4] += [i]
        if x[0] == "XXXL":
            L[5] += [i]
a = 0
ok = 1
R = ["" for _ in range(n)]

# S
if len(L[0]) <= T[0]:
    for x in L[0]:
        R[x] = "S"
    T[0] -= len(L[0])
else:
    print("NO")
    ok = 0

a = max(0, len(D[0]) - T[0])
for i in range(min(len(D[0]), T[0])):
    R[D[0][i]] = "S"

# M
if a + len(L[1]) <= T[1]:
    for i in range(len(D[0]) - a, len(D[0])):
        R[D[0][i]] = "M"
    for x in L[1]:
        R[x] = "M"
    T[1] -= len(L[1]) + a
else:
    print("NO")
    ok = 0

a = max(0, len(D[1]) - T[1])
for i in range(min(len(D[1]), T[1])):
    R[D[1][i]] = "M"

# L
if a + len(L[2]) <= T[2]:
    for i in range(len(D[1]) - a, len(D[1])):
        R[D[1][i]] = "L"
    for x in L[2]:
        R[x] = "L"
    T[2] -= len(L[2]) + a
else:
    print("NO")
    ok = 0

a = max(0, len(D[2]) - T[2])
for i in range(min(len(D[2]), T[2])):
    R[D[2][i]] = "L"

# XL
if a + len(L[3]) <= T[3]:
    for i in range(len(D[2]) - a, len(D[2])):
        R[D[2][i]] = "XL"
    for x in L[3]:
        R[x] = "XL"
    T[3] -= len(L[3]) + a
else:
    print("NO")
    ok = 0

a = max(0, len(D[3]) - T[3])
for i in range(min(len(D[3]), T[3])):
    R[D[3][i]] = "XL"

# XXL
if a + len(L[4]) <= T[4]:
    for i in range(len(D[3]) - a, len(D[3])):
        R[D[3][i]] = "XXL"
    for x in L[4]:
        R[x] = "XXL"
    T[4] -= len(L[4]) + a
else:
    print("NO")
    ok = 0

a = max(0, len(D[4]) - T[4])
for i in range(min(len(D[4]), T[4])):
    R[D[4][i]] = "XXL"

# XXXL
if a + len(L[5]) <= T[5]:
    for i in range(len(D[4]) - a, len(D[4])):
        R[D[4][i]] = "XXXL"
    for x in L[5]:
        R[x] = "XXXL"
else:
    print("NO")
    ok = 0

if ok:
    print("YES")
    for i in range(n):
        print(R[i])
