N = int(input())
A = [int(n) for n in input().split()]
if len(set(A)) == N:
    print('YES')
else:
    print('NO')
