t = int(input())
while t:
    t -= 1
    (n, k) = list(map(int, input().split()))
    a = [int(i) for i in input().split()]
    a.sort()
    ans = 0
    a.reverse()
    for i in range(k + 1):
        ans += a[i]
    print(ans)
