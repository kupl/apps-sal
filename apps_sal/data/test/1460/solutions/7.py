for _ in range(1):
    # a, b, n = map(int, input().split())
    k = int(input())
    # arr = list(map(int, input().split()))
    arr = [(0, 0), (0, 1)]
    c = [0, 0]
    for i in range(k):
        c[0] += 1
        c[1] += 1
        arr.append([c[0], c[1] - 1])
        arr.append([c[0], c[1]])
        arr.append([c[0], c[1] + 1])
    arr.append([c[0] + 1, c[1]])
    arr.append([c[0] + 1, c[1] + 1])
    print(len(arr))
    for el in arr:
        print(*el)
