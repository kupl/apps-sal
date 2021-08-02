t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ga = 0
    for i in range(1, 2 * n + 1):
        j, k = 0, n - 1
        flag = True
        ans = 0
        while(j < k):
            if a[j] + a[k] > i:
                k -= 1
            elif a[j] + a[k] < i:
                j += 1
            else:
                j += 1
                k -= 1
                ans += 1
        ga = max(ans, ga)
    print(ga)
