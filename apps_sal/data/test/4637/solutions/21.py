t = int(input())
for i in range(t):
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    b.reverse()
    ans = sum(a)
    for i in range(k):
        if a[i] < b[i]:
            ans += b[i] - a[i]
    print(ans)
