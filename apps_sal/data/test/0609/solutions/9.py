n = int(input())
A = [input() for _ in range(n)]
x = A[0][0]
a = A[0][1]
if x != a:
    msg = 'YES'
    for i in range(n):
        for j in range(n):
            if i == j or i == n - j - 1:
                if A[i][j] != x:
                    msg = 'NO'
                    break
            elif A[i][j] != a:
                msg = 'NO'
                break
else:
    msg = 'NO'
print(msg)
