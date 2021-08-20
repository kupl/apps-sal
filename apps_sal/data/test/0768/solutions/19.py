s = input().split()
(F, I, T) = (int(s[i]) for i in range(3))
a = [''] * F
for i in range(F):
    a[i] = input()
r = 0
for i in range(I):
    c = 0
    for j in range(F):
        c += a[j][i] == 'Y'
    r += c >= T
print(r)
kitten = 0
