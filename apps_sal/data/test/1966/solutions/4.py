n = int(input())

A = []
for _ in range(n):
    A.append(input())
blank = input()

B = []
for _ in range(n):
    B.append(input())
blank = input()

C = []
for _ in range(n):
    C.append(input())
blank = input()

D = []
for _ in range(n):
    D.append(input())

ret = 999999
cnt = 0
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if A[i][j] == "0":
                cnt += 1
        else:
            if A[i][j] == "1":
                cnt += 1
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if B[i][j] == "0":
                cnt += 1
        else:
            if B[i][j] == "1":
                cnt += 1
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if C[i][j] == "1":
                cnt += 1
        else:
            if C[i][j] == "0":
                cnt += 1
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if D[i][j] == "1":
                cnt += 1
        else:
            if D[i][j] == "0":
                cnt += 1
ret = min(ret, cnt)
cnt = 0
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if A[i][j] == "0":
                cnt += 1
        else:
            if A[i][j] == "1":
                cnt += 1
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if C[i][j] == "0":
                cnt += 1
        else:
            if C[i][j] == "1":
                cnt += 1
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if B[i][j] == "1":
                cnt += 1
        else:
            if B[i][j] == "0":
                cnt += 1
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if D[i][j] == "1":
                cnt += 1
        else:
            if D[i][j] == "0":
                cnt += 1
ret = min(ret, cnt)
cnt = 0
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if A[i][j] == "0":
                cnt += 1
        else:
            if A[i][j] == "1":
                cnt += 1
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if D[i][j] == "0":
                cnt += 1
        else:
            if D[i][j] == "1":
                cnt += 1
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if C[i][j] == "1":
                cnt += 1
        else:
            if C[i][j] == "0":
                cnt += 1
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if B[i][j] == "1":
                cnt += 1
        else:
            if B[i][j] == "0":
                cnt += 1
ret = min(ret, cnt)
cnt = 0
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if B[i][j] == "0":
                cnt += 1
        else:
            if B[i][j] == "1":
                cnt += 1
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if C[i][j] == "0":
                cnt += 1
        else:
            if C[i][j] == "1":
                cnt += 1
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if A[i][j] == "1":
                cnt += 1
        else:
            if A[i][j] == "0":
                cnt += 1
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if D[i][j] == "1":
                cnt += 1
        else:
            if D[i][j] == "0":
                cnt += 1
ret = min(ret, cnt)
cnt = 0
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if D[i][j] == "0":
                cnt += 1
        else:
            if D[i][j] == "1":
                cnt += 1
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if B[i][j] == "0":
                cnt += 1
        else:
            if B[i][j] == "1":
                cnt += 1
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if C[i][j] == "1":
                cnt += 1
        else:
            if C[i][j] == "0":
                cnt += 1
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if A[i][j] == "1":
                cnt += 1
        else:
            if A[i][j] == "0":
                cnt += 1
ret = min(ret, cnt)
cnt = 0
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if C[i][j] == "0":
                cnt += 1
        else:
            if C[i][j] == "1":
                cnt += 1
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if D[i][j] == "0":
                cnt += 1
        else:
            if D[i][j] == "1":
                cnt += 1
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if A[i][j] == "1":
                cnt += 1
        else:
            if A[i][j] == "0":
                cnt += 1
for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            if B[i][j] == "1":
                cnt += 1
        else:
            if B[i][j] == "0":
                cnt += 1
ret = min(ret, cnt)
cnt = 0
print(ret)
