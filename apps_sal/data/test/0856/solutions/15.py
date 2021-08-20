t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    s = max(a)
    t = min(a)
    ans = []
    if k % 2 == 0:
        for i in range(n):
            ans.append(str(a[i] - t))
    else:
        for i in range(n):
            ans.append(str(s - a[i]))
    print(' '.join(ans))
