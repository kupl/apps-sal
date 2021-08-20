c = []
(F, I, T) = map(int, input().split())
for i in range(F):
    s = input()
    for j in range(I):
        c.append(0)
        c[j] += s[j] == 'Y'
r = 0
for i in range(I):
    r += c[i] >= T
print(r)
kitten = 0
