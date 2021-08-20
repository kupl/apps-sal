(n, k) = map(int, input().split())
m = 1
if n == 1:
    print(k)
else:
    m *= k
    for i in range(n - 1):
        m *= k - 1
    print(m)
