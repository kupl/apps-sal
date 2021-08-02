n, m = map(int, input().split())
x = sorted(list(map(int, input().split())))

if n >= m: print(0)
else:
    dist = [abs(x[i + 1] - x[i]) for i in range(m - 1)]
    dist = sorted(dist)
    print(sum(dist[:m - n]))
