try:
    while True:
        n = int(input())
        d = [0] * 4000
        for i in range(n):
            (x, y) = list(map(int, input().split()))
            d[x + y] += 1
            d[y - x + 3000] += 1
        print(sum((0 if x < 2 else x * (x - 1) >> 1 for x in d)))
except EOFError:
    pass
