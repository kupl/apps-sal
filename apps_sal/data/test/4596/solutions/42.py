def resolve():
    _ = int(input())
    a = list(map(int, input().split()))
    res = 0
    while all(i % 2 == 0 for i in a):
        res += 1
        a = list(map(lambda x: x / 2, a))
    print(res)


resolve()
