for t in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    if sum(x) == n:
        if n % 2:
            print('First')
        else:
            print('Second')
    else:
        i = 0
        while x[i] == 1:
            i += 1
        if i % 2:
            print('Second')
        else:
            print('First')
