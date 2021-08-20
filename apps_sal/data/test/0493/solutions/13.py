n = int(input())
s = input()
c = n
k = 0
(l, r) = (0, 0)
for i in range(n):
    if s[i] == '.':
        continue
    if s[i] == 'L':
        k -= 1
        l = i
    else:
        k += 1
        r = i
    if k < 0:
        c -= i + 1
        k = 0
    elif k == 0:
        c -= l - r + 1 - (l - r + 1) % 2
if k > 0:
    c -= n - r
print(c)
