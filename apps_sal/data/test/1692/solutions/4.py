s = [ord(c) - 48 for c in input()]
n = len(s)
ans = s.count(0) + s.count(4) + s.count(8)
for i in range(1, n):
    if (s[i-1]*10 + s[i]) % 4 == 0: ans += i
print(ans)

