for t in range(int(input())):
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    print(a[n] - a[n - 1])
