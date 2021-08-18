
n = int(input())

arr = []

for i in range(n - 1):
    arr.append(list(map(int, input().strip().split())))
mp = {}

ans = []
for i in range(n - 1):
    a = arr[i][0]
    b = arr[i][1]

    if (a not in mp) and (b not in mp):
        mp[a] = len(ans)
        mp[b] = len(ans)
        ans.append([a, b])
    else:
        if (a in mp) and (b not in mp):
            ans[mp[a]].append(b)
            mp[b] = mp[a]
        else:
            if (a not in mp) and (b in mp):
                ans[mp[b]].append(a)
                mp[a] = mp[b]
            else:
                ans[mp[a]].extend(ans[mp[b]])
                for x in ans[mp[b]]:
                    mp[x] = mp[a]
for i in range(len(ans)):
    if len(ans[i]) == n:
        print(*ans[i])
        break
