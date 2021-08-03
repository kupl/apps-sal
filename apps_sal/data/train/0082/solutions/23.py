for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = arr[-1::-1]
    print(*arr)
