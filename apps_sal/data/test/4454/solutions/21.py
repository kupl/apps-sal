for c in range(int(input())) :
    n = int(input())
    a = list(map(int, input().split()))
    tot = sum(a)
    print( (tot + n - 1) // n )

