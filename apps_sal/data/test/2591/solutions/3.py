t = int(input())
for q in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = []
    for i in range(0, n // 2):
        b.append(a[i])
        b.append(a[n - i - 1])
    if n % 2 != 0:
        b.append(a[n // 2])
    b.reverse()
    print(*b)

