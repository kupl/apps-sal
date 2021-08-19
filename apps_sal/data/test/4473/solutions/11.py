def I():
    return list(map(int, input().split()))


for _ in range(int(input())):
    (a, b, k) = I()
    if k % 2 == 0:
        print(k // 2 * (a - b))
    else:
        print(k // 2 * (a - b) + a)
