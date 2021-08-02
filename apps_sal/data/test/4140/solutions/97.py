s = list(input())
ans = 1e5
for i0 in range(2):
    sum = 0
    for i in range(len(s)):
        x = i + i0
        if str(x % 2) == s[i]: sum += 1
    ans = min(sum, ans)
print(ans)
