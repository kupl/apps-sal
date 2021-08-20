s = input()
a = [0] * 26
b = [0] * 26
for c in 'nineteen':
    a[ord(c) - ord('a')] += 1
for c in s:
    b[ord(c) - ord('a')] += 1
s = 0
if all((y >= x for (x, y) in zip(a, b))):
    s += 1
    for i in range(26):
        b[i] -= a[i]
    a[ord('n') - ord('a')] -= 1
    s += min((y // x for (x, y) in zip(a, b) if x > 0))
print(s)
