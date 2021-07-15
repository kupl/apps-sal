__author__ = 'Rakshak.R.Hegde'
n = int(input())
m = dict()
s = [0] * (2 * n)
xor2 = 0
ind = 0
for i in range(n):
    a, b = map(int, input().split())
    xor2 ^= a ^ b
    s[ind] = a
    ind += 1
    s[ind] = b
    ind += 1
    m[a] = b
l = r = 0
setBit = xor2 & ~(xor2 - 1)
for i in s:
    if i & setBit:
        l ^= i
    else:
        r ^= i
if l not in m: l = r
a, b = 0, l
ans = str(b)
for i in range(1, n, 2):
    a = m[a]
    ans += ' ' + str(a)
    b = m[b]
    if b != 0:
        ans += ' ' + str(b)
print(ans)
