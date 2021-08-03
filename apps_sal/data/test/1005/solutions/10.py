t = int(input())
for i in range(t):
    n, k, d = map(int, input().split())
    minn = k
    a = [int(i) for i in input().split()]
    for i in range(n - d + 1):
        m = set(a[i:i + d])
        minn = min(minn, len(m))
    print(minn)
