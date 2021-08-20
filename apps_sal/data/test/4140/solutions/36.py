s = input()
l = len(s)
(a, b) = ('', '')
for i in range(l):
    if i % 2 == 0:
        a += '1'
        b += '0'
    else:
        a += '0'
        b += '1'
(diff_a, diff_b) = (0, 0)
for i in range(l):
    if a[i] != s[i]:
        diff_a += 1
    if b[i] != s[i]:
        diff_b += 1
print(min(diff_a, diff_b))
