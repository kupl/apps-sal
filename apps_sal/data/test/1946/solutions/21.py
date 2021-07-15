def solution():
    n = int(input())
    d1, d2 = dict(), dict()
    for _ in range(n):
        key, value = list(map(int, input().split()))
        d1[key] = value
    m = int(input())
    for _ in range(m):
        key, value = list(map(int, input().split()))
        d2[key] = value

    for key, value in list(d2.items()):
        if key in d1:
            if d2[key] > d1[key]:
                d1[key] = value
        else:
            d1[key] = value
    print(sum(d1.values()))



solution()

