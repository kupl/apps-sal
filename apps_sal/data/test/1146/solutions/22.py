n, m = list(map(int, input().split()))
lst = [False] * m
for i in range(n):
    k = list(map(int, input().split()))
    for i in range(1, len(k)):
        lst[k[i] - 1] = True
    
for i in lst:
    if i == False:
        print('NO')
        break
else:
    print('YES')

