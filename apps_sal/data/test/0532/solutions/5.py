def d(x, y):
    return min(abs(ord(x) - ord(y)), 26 - abs(ord(x) - ord(y)))


ans = 0
s = 'a' + input()
for i in range(len(s) - 1):
    ans += d(s[i], s[i + 1])
print(ans)
