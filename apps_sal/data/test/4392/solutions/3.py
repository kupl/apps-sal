t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    p = set(list(map(int, input().split())))
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1] and j + 1 in p:
                a[j], a[j + 1] = a[j + 1], a[j]
    if a == sorted(a):
        print("YES")
    else:
        print("NO")
