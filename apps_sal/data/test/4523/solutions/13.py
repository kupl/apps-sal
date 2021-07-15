ans = []
for _ in range(int(input())):
    n = int(input())
    u = list(map(int, input().split()))
    u.sort()
    for i in range(1, n):
        if u[i] - u[i - 1] > 1:
            print('NO')
            break
    else:
        print('YES')

