t = int(input())
for i in range(t):
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))
    a.sort()
    a.reverse()
    w.sort()
    ans = 0
    for i in range(k):
        ans += a[i]
    pointer = k - 1
    for i in range(k):
        if w[i] == 1:
            ans += a[i]
            continue
        pointer += w[i] - 1
        ans += a[pointer]
    print(ans)
