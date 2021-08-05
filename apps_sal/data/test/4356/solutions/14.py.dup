n, m = map(int, input().split())
A = [input() for i in range(n)]
B = [input() for i in range(m)]

flag = False
for i in range(n - m + 1):
    for j in range(n - m + 1):
        flag = True
        for k in range(m):
            if B[k] != A[i + k][j:j + m]:
                flag = False
        if flag:
            print("Yes")
            return
print("No")
