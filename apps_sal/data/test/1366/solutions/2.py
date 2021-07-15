n = int(input())
A = []

for i in range(n):
    A.append(list(map(int, input().split())))
res = 0

for i in range(n):
    flag = 0

    for j in range(n):
        if A[j][1] == A[i][0] and i != j:
            flag = 1
    res += 1 - flag
print(res)

