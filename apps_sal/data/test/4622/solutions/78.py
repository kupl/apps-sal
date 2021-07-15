N = int(input())
A = list(map(int, input().split()))

if N == len(set(A)):
    print('YES')
else:
    print('NO')
