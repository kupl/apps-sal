n, k = map(int, input().split())
for i in range(1, n+1):
    a, b = i*2, i*2-1
    if k:
        a, b = b, a
        k -= 1
    print(a, b, end=' ')

