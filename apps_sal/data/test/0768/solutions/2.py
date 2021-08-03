f, I, t = list(map(int, input().split()))
c = [0] * I
for kitten in range(f):
    s = input()
    for j in range(I):
        if s[j] == 'Y':
            c[j] += 1
q = 0
for j in range(I):
    if c[j] >= t:
        q += 1
print(q)
