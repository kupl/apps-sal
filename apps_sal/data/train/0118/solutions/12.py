t = int(input())
for _ in range(t):
    (n, x) = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    count = 0
    ans = 0
    for i in range(n):
        count += 1
        if count * a[i] >= x:
            ans += 1
            count = 0
    print(ans)
