def check(A, sum, n):
    if n == 0:
        if sum % 360 == 0:
            return True
        else:
            return False
    else:
        return check(A[1:], sum + A[0], n - 1) or check(A[1:], sum - A[0], n - 1)


n = int(input())
A = []
for _ in range(n):
    x = int(input())
    A.append(x)
if check(A, 0, n):
    print('YES')
else:
    print('NO')
