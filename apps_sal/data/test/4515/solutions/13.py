
T = int(input())
for _ in range(T):
    a, b, c, n = list(map(int, input().split()))
    mx = max(a, b, c)
    tot = mx - a + mx - b + mx - c

    if(n < tot):
        print('NO')
    else:
        n = n - tot
        if(n % 3 == 0):
            print('YES')
        else:
            print('NO')
