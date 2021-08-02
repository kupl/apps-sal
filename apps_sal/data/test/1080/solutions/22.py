a = int(input())
A = list(map(int, input().split()))
m = max(A)
s = sum(A)
if s - m >= m and s % 2 == 0:
    print('YES')
else:
    print('NO')
