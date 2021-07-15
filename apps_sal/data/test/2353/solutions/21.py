for _ in range(int(input())):
    a, b, c, d = list(map(int, input().split()))
    if a > b and d >= c:
        print(-1)
        continue

    if b >= a:
        print(b)
        continue

    diff = a-b
    step = c-d

    howmany = (diff+step-1)//step
    print(b + howmany * c)

