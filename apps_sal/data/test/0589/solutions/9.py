s = input()


ans = 1
table = [0] * 26
for c in s:
    if c == '?':
        ans *= 10
    elif 'A' <= c <= 'J':
        table[ord(c) - ord('A')] += 1

total = 0
for c in range(26):
    if table[c]:
        total += 1

for i in range(total):
    ans *= 10 - i
if 'A' <= s[0] <= 'J':
    ans = ans // 10 * 9
if s[0] == '?':
    ans = ans // 10 * 9
print(ans)
