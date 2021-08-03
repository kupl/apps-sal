n, m, k = map(int, input().split())
b = [int(i) for i in input().split()]
if k == 1:
    print(b[-1] - b[0] + 1)
else:
    d = [b[i] - b[i - 1] for i in range(1, n)]
    d.sort()
    d = d[:-k + 1]
    print(sum(d) + k)
