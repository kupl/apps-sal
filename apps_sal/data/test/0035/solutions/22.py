n, m = map(int, input().split())
A = [0 for i in range(n)]
for i in range(n):
    A[i] = input()

f1, f2 = True, True

colors = ["R", "G", "B"]
if n % 3 != 0:
    f1 = False
else:
    for i in range(3):
        if A[n//3 * i][0] in colors:
            qq = A[n//3 * i][0]
            colors.remove(A[n//3 * i][0])
        else:
            f1 = False
        for j in range(n//3 * i, n//3 *(i + 1) ):
            if A[j][0] != qq:
                f1 = False
                break
            for k in A[j]:
                if k != A[j][0]:
                    f1 = False
                    break
colors = ["R", "G", "B"]
if m % 3 != 0:
    f2 = False
else:
    for i in range(3):
        if A[0][m // 3 * i] in colors:
            qq = A[0][m // 3 * i]
            colors.remove(A[0][m // 3 * i])
        else:
            f2 = False
        
        for j in range(m//3 * i, m//3 *(i + 1) ):
            if A[0][j] != qq:
                f2 = False
                break
            for k in range(n):
                if A[k][j] != A[0][j]:
                    f2 = False
                    break



if f1 or f2:
    print("YES")
else:
    print("NO")
