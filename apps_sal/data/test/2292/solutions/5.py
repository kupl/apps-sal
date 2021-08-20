for _ in range(int(input())):
    n = int(input())
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))
    if sorted(zip(a, reversed(a))) == sorted(zip(b, reversed(b))):
        print('Yes')
    else:
        print('No')
