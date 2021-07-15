for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    j = a.copy()
    a.sort()
    if 1 in b and 0 in b:
        print('Yes')
    elif j == a:
        print('Yes')
    else:
        print('No')
