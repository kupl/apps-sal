for i in range(int(input())):
    a = sorted([int(i) for i in input().split()])
    print(min(a[0] + a[1], sum(a) // 2))
