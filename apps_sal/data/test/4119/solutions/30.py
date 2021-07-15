n, m = list(map(int, input().split()))
x = sorted(list(map(int, input().split())))

gaps = [x[i] - x[i-1] for i in range(1, len(x))]

if n == 1:
    print((sum(gaps)))
else:
    print((sum(sorted(gaps)[:-n+1])))

