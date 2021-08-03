def Volume(s):
    ans = 0
    for x in s:
        if x >= 'A' and x <= 'Z':
            ans += 1
    return ans


n = int(input())
Text = list(map(str, input().split()))
ans = 0
for x in Text:
    ans = max(ans, Volume(x))
print(ans)
