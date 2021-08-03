def prime(n):
    if n < 2:
        return False
    elif n % 2 == 0:
        return False
    else:
        for k in range(3, 1 + int(n ** .5), 2):
            if n % k == 0:
                return False
    return True


t = int(input())
for i in range(t):
    a, b = list(map(int, input().split()))
    n = (a + b)
    if a - b > 1:
        print('NO')
    else:
        if prime(n):
            print('YES')
        else:
            print('NO')
