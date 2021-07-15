n, m = list(map(int, input().split()))
A = []
B = []
Acount = []
Bcount = []
for i in range(n):
    A.append(list(map(int, input().split())))

for i in range(n):
    B.append(list(map(int, input().split())))

for i in range(n):
    count = 0
    for j in range(m):
        if A[i][j] == 1:
            count += 1
    Acount.append(count)
for i in range(m):
    count = 0
    for j in range(n):
        if A[j][i] == 1:
            count += 1
    Acount.append(count)

for i in range(n):
    count = 0
    for j in range(m):
        if B[i][j] == 1:
            count += 1
    Bcount.append(count)
for i in range(m):
    count = 0
    for j in range(n):
        if B[j][i] == 1:
            count += 1
    Bcount.append(count)

flag = 1
for i in range(n+m):
    if (Acount[i] - Bcount[i]) % 2 == 1:
        flag = 0
if flag == 1:
    print("Yes")
else:
    print("No")

