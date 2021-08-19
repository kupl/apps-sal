for i in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    p.reverse()
    print(' '.join((str(num) for num in p)))
