t = int(input())
for q in range(t):
    (n, k, d) = map(int, input().split())
    a = [int(i) for i in input().split()]
    m = n
    for i in range(0, n - d + 1):
        if len(set(a[i:i + d])) < m:
            m = len(set(a[i:i + d]))
    print(m)
