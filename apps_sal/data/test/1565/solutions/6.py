n = int(input())
s = input()
l = int(n / 2)
r = int((n + 1) / 2)
while (l and s[l] == '0'):
    l -= 1
while (r != n - 1 and s[r] == '0'):
    r += 1
if (l == 0 or r == n - 1):
    if (l == 0):
        ans = int(s[:r]) + int(s[r:])
    else:
        ans = int(s[:l]) + int(s[l:])
else:
    ans = min(int(s[:l]) + int(s[l:]), int(s[:r]) + int(s[r:]))
print(ans)
