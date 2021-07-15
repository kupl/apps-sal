n = int(input())
plist = list(map(int, input().split()))

ans = 0
for i in range(1, n-1):
    if max(plist[i-1], plist[i], plist[i+1]) != plist[i] and min(plist[i-1], plist[i], plist[i+1]) != plist[i]:
        ans += 1
print(ans)
