n = int(input())
a = list(map(int, input().split())) + [0]
s, sb, val = [], 0, 0
for i in range(1, n + 1):
    if a[i] <= a[i - 1]:
        s.append((sb, i - 1))
        val = max(val, i - sb)
        sb = i
val += len(s) > 1
for i in range(1, len(s)):
    c = s[i][0]
    if c in range(2, n - 1) and max(a[c] - a[c - 2], a[c + 1] - a[c - 1]) >= 2:
        val = max(val, s[i][1] - s[i - 1][0] + 1)
print(val)
