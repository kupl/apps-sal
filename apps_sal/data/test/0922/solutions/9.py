n, A = map(int, input().split())
d = list(map(int, input().split()))
s = sum(d)
for i in range(n):
    k = max(A + d[i] - s - 1, 0)
    l = max(d[i] - A + n - 1, 0)
    print(k + l, end=' ')
