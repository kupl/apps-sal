def solve(n, k):
    print(1 * k, end=' ')
    if n == 2:
        print(2 * k, end=' ')
    if n == 3:
        print(k, 3 * k, end=' ')
    else:
        temp = n // 2
        if(n % 2 == 0):
            temp -= 1
        print((str(k) + ' ') * temp, end='')
        if(n > 3):
            solve(n // 2, k * 2)


n = int(input())
solve(n, 1)
