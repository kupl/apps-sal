n = int(input())
N = [0, 0, 0, 0]
for i in range(4):
    for j in range(n):
        t = input()
        for k in range(n):
            if int(t[k]) == (j+k)%2:
                N[i] += 1
    if i != 3:
        s = input()
M = [0, 0, 0, 0]
for i in range(4):
    M[i] = (n * n) - N[i]
L = [0] * 6
L[0] = N[0] + N[1] + M[2] + M[3]
L[1] = N[0] + N[2] + M[1] + M[3]
L[2] = N[0] + N[3] + M[1] + M[2]
L[3] = N[1] + N[2] + M[0] + M[3]
L[4] = N[1] + N[3] + M[0] + M[2]
L[5] = N[2] + N[3] + M[0] + M[1]
mn = L[0]
for i in range(1, 6):
    if L[i] < mn:
        mn = L[i]
print(mn)

