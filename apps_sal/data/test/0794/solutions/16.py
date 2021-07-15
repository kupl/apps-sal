n = int(input())

xs = sorted(map(int, input().split()))

if sum(xs[:n]) != sum(xs[n:]):
    print(' '.join(map(str, xs)))
else:
    print(-1)

