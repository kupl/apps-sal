t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    m = a[0]
    a = a[1:]
    total = 0
    for b in a:
        total += (k-b)//m

    print(total)
