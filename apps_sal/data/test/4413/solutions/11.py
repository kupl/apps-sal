q = int(input())
for query in range(q):
    n = int(input())
    a = list(map(int, input().split(" ")))
    a = sorted(a)
    res = 1
    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) == 1:
            res = 2
            break
    print(res)
