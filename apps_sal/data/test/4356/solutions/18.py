n, m = map(int, input().split())
A = [list(input()) for i in range(n)]
B = [list(input()) for i in range(m)]
for i in range(n - m + 1):
    for j in range(n - m + 1):
        flag = True
        for k in range(m):
            if A[k + j][i:i + m] != B[k][:]:
                flag = False
                break
        if flag:
            print("Yes")
            return
else:
    print("No")
