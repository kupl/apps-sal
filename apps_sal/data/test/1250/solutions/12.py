n = int(input())
if n < 3:
    print(-1)
else:
    print(' '.join(list(map(str, list(range(n, 0, -1))))))
