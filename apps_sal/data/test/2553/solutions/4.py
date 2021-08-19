for t in range(int(input())):
    (n, x) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    odd = sum(map(lambda x: x % 2 == 1, a))
    even = sum(map(lambda x: x % 2 == 0, a))
    total = sum(a) % 2
    if x == n:
        if total:
            print('Yes')
        else:
            print('No')
    elif odd == 0:
        print('No')
    elif x % 2 == 1:
        print('Yes')
    elif even:
        print('Yes')
    else:
        print('No')
