for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    s = sorted(list(map(int, input().split())))
    print(*a)
    print(*s)
