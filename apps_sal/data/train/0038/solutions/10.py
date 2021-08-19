t = int(input())
for i in range(t):
    (n, k1, k2) = list(map(int, input().split()))
    a = max(list(map(int, input().split())))
    b = max(list(map(int, input().split())))
    if a > b:
        print('YES')
    else:
        print('NO')
