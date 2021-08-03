n, a, b = list(map(int, input().split()))
if a * b < n:
    print(-1)
else:
    chairs = list(map(str, list(range(1, n + 1)) + [0] * (a * b - n)))
    for i, (start, end) in enumerate(zip(list(range(0, a * b, b)), list(range(b, a * b + 1, b)))):
        if i % 2:
            print(' '.join(reversed(chairs[start:end])))
        else:
            print(' '.join(chairs[start:end]))
