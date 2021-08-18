n = int(input())
s1 = input()
s2a = ''
da = 0
ar = 0
ab = 0
s2b = ''
db = 0
br = 0
bb = 0
pairs = int(n // 2)
carry = n % 2
for _ in range(pairs):
    s2a += 'rb'
    s2b += 'br'
if carry:
    s2a += 'r'
    s2b += 'b'

if s1 == s2a or s1 == s2b:
    print(0)
    return

for i in range(n):
    if not s1[i] == s2a[i]:
        da += 1
        if s1[i] == 'r':
            ar += 1
        else:
            ab += 1
    if not s1[i] == s2b[i]:
        db += 1
        if s1[i] == 'r':
            br += 1
        else:
            bb += 1

da -= min(ar, ab)
db -= min(br, bb)
print(min(da, db))
