q = int(input())
for query in range(q):
    (n, k) = list(map(int, input().split()))
    l = list(map(int, input().split()))
    a = min(l)
    b = max(l)
    if b - a <= 2 * k:
        print(a + k)
    else:
        print(-1)
