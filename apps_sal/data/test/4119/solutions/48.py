n, m = map(int, input().split())
x = sorted(list(map(int, input().split())))
d = []
if n >= m or m == 1:
    print(0)
elif n < m:
    for i in range(m - 1):
        d.append(x[i + 1] - x[i])
    print(sum(sorted(d)[:m - n]))
