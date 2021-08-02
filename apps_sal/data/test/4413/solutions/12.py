q = int(input())
for _ in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    f = 1
    for i in range(1, n):
        if a[i - 1] + 1 == a[i]:
            f = 2
            break
    print(f)
