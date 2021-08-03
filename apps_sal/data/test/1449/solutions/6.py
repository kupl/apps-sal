t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 1
    for i in range(n - 1):
        if a[i + 1] > a[i]:
            ans += 1
    if ans <= k:
        print(1)
    elif k == 1:
        print(-1)
    else:
        print((ans - k - 1) // (k - 1) + 2)
