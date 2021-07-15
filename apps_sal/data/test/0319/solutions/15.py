T = input().split(' ')
n = int(T[0])
m = int(T[1])
S = [0] * n
Q = []
for i in range(n):
    Q.append(input())
for i in range(m):
    a = -1
    b = -1
    for j in range(n):
        if Q[j][i] == '1':
            if a==-1:
                a=j
            else:
                b=j
                break
    if a!=-1 and b==-1:
        S[a] = 1
b = False
for j in range(n):
    if S[j] == 0:
        b = True
        break
if b:
    print("YES")
else:
    print("NO")

