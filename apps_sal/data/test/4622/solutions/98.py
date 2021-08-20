N = int(input())
A = [int(x) for x in input().split()]
if len(set(A)) == len(A):
    print('YES')
else:
    print('NO')
