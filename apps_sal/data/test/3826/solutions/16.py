n = int(input())
a = list(map(int, input().split()))
k = set(a)
m = len(k)
if n == m:
    print(0)
else:
    ans = 9999999999999999999999999999999999999999999999999999999999999999
    for i in range(n):
        mp = {}
        for j in range(n):
            if a[j] in mp:
                mp[a[j]] += 1
            else:
                mp[a[j]] = 1
        for j in range(i, n):
            mp[a[j]] -= 1
            if mp[a[j]] == 0:
                mp.pop(a[j])
            p = len(mp)
            if p == n - j + i - 1:
                ans = min(ans, j - i + 1)
                break
    print(ans)
