from collections import Counter
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
mod = 2019


s = readline().decode().rstrip()
s = s[::-1]
n = len(s)
d = [0] * (n)
d[0] = int(s[0]) % mod

for i in range(1, n):
    d[i] = (d[i - 1] + int(s[i]) * pow(10, i, mod)) % mod

d = [0] + d

c = Counter(d)
ans = 0
for v in c.values():
    ans += v * (v - 1) // 2
print(ans)
