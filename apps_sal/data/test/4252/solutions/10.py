n = int(input())
s = input()
ans, l = 0, -2
for i in range(len(s)):
    if s[i] == 'x':
        l += 1
    else:
        ans += max(0, l)
        l = -2
print(ans + max(0, l))
