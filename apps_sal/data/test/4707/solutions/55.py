def getints():
    return list(map(int, input().split()))


s = input()
ans = 0
for c in s:
    if c == '1':
        ans += 1
print(ans)
