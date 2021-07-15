def __starting_point():
    t = int(input())
    while t:
        t -= 1
        n, m = map(int, input().split())
        a = [int(x) for x in input().split()]
        sum = 0
        for i in a:
            sum += i
        if sum == m:
            print('YES')
        else:
            print('NO')
__starting_point()
