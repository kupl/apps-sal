t = int(input())
for q in range(0, t):
    (n, k) = map(int, input().split())
    if n == k == 2:
        print('YES')
    elif n == 1 or k == 1:
        print('YES')
    else:
        print('NO')
