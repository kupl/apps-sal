q = int(input())
for i in range(q):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    ans = 1
    for i in range(1, n):
        if a[i] - a[i - 1] == 1:
            ans = 2
    print(ans)
