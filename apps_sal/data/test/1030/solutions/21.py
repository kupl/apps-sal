(n, p, k) = list(map(int, input().split()))
s = '({})'.format(p)
for i in range(1, k + 1):
    if p - i > 0:
        s = str(p - i) + ' ' + s
    if p + i <= n:
        s = s + ' ' + str(p + i)
if p - k > 1:
    s = '<< ' + s
if p + k < n:
    s = s + ' >>'
print(s)
