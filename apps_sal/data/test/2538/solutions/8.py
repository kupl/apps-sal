for _ in range(int(input())):
    s, i, e = list(map(int, input().split()))
    if s + e <= i:
        print('0')
    elif s > i + e:
        print(e + 1)
    else:
        print((e + s + 1 - i) // 2)
