a, f, ii, n, s = 0, 0, 0, int(input()), str(input())
for i in range(n):
    if s[i] == 'I':
        ii += 1
    if s[i] == 'A':
        a += 1
    if s[i] == 'F':
        f += 1
if ii > 1:
    ii = 0
print(a if s.find('I') == -1 else ii)
