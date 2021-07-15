n = int(input())
A = list(map(int,input().split()))
UA = set(A)
print('YES' if len(A) == len(UA) else 'NO')
