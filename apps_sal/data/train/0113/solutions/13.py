for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    target = abs(a - b)
    res = 0

    res += target // 5
    target = target % 5
    res += target // 2
    target = target % 2
    res += target // 1
    target = target % 1

    print(res)
