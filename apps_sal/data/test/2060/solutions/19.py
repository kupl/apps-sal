def read(): return list(map(int, input().split()))


n = int(input())
for i in range(n):
    x = int(input())
    if x not in [1, 2, 4, 5, 8, 11]:
        print('YES')
    else:
        print('NO')
