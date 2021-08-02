n, m = list(map(int, input().split()))
if n > m:
    n, m = m, n
res = str(n)
print((res * m))
