read = lambda: map(int, input().split())
a = input()
b = input()
low = lambda c: chr(ord(c) + ord('a') - ord('A'))
hig = lambda c: chr(ord(c) - ord('a') + ord('A'))
ish = lambda c: ord('A') <= ord(c) <= ord('Z')
f = lambda c: b[a.index(c)]
s = input()
ans = [''] * len(s)
for i in range(len(s)):
    c = s[i]
    if ord('0') <= ord(c) <= ord('9'):
        ans[i] = c
        continue
    if ish(c):
        ans[i] = hig(f(low(c)))
    else: ans[i] = f(c)
print(''.join(ans))
