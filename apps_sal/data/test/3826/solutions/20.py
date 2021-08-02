n = int(input())
a = [int(x) for x in input().split()]
mp = {}
rep = 0

for i in range(n):
    if a[i] in mp:
        mp[a[i]] += 1
        rep += 1
    else:
        mp[a[i]] = 1

ans = 1000000
if rep == 0:
    print(0)
else:
    for i in range(n):
        z = []
        flag = 0
        for j in range(i, n):
            if mp[a[j]] > 1:
                z.append(a[j])
                mp[a[j]] -= 1
                rep -= 1
            if rep == 0:
                ans = min(ans, j - i + 1)
                break
        rep += len(z)
        for i in z:
            mp[i] += 1
    print(ans)
