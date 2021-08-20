(n, x, y) = input().split()
ans = 0
s = input()
s = s[::-1]
s = s[:int(x)]
for i in range(0, len(s)):
    if i == int(y):
        if s[i] == '0':
            ans += 1
    elif s[i] == '1':
        ans += 1
print(ans)
