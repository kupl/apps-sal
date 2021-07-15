for __ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    ar.reverse()
    print(*ar)
