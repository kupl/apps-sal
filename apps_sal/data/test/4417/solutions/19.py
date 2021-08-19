q = int(input())
for _ in range(q):
    (n, k) = map(int, input().split())
    a = [int(i) for i in input().split()]
    a.sort()
    if a[-1] - a[0] > 2 * k:
        print(-1)
    else:
        print(a[0] + k)
