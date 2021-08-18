
try:
    while True:
        n, m = list(map(int, input().split()))
        result = 0
        for i in range(n):
            a = list(map(int, input().split()))
            for j in range(m):
                if a[j << 1] or a[j << 1 | 0x1]:
                    result += 1
        print(result)
except EOFError:
    pass
