N = int(input())
lst = list(map(int, input().split()))
k = list(set(lst))
if len(k) == N:
    print('YES')
else:
    print('NO')
