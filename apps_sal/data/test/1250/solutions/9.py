n = int(input())
if n <= 2:
    print(-1)
else:
    print(' '.join(map(str, list(range(2, n + 1)) + [1])))
