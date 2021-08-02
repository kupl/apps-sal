for _ in range(int(input())):
    n = int(input())
    li = sorted(list(map(int, input().split())))
    print(min(li[n - 2] - 1, n - 2))
