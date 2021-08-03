def read(): return map(int, input().split())


a = input()
b = input()
def low(c): return chr(ord(c) + ord('a') - ord('A'))
def hig(c): return chr(ord(c) - ord('a') + ord('A'))
def ish(c): return ord('A') <= ord(c) <= ord('Z')
def f(c): return b[a.index(c)]


s = input()
ans = [''] * len(s)
for i in range(len(s)):
    c = s[i]
    if ord('0') <= ord(c) <= ord('9'):
        ans[i] = c
        continue
    if ish(c):
        ans[i] = hig(f(low(c)))
    else:
        ans[i] = f(c)
print(''.join(ans))
