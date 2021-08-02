n, k = map(int, input().split())
s = str(input())
if s[k - 1] == 'A':
    ans = s[:k - 1] + 'a' + s[k:]
elif s[k - 1] == 'B':
    ans = s[:k - 1] + 'b' + s[k:]
else:
    ans = s[:k - 1] + 'c' + s[k:]
print(ans)
