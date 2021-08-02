n = int(input())
c = [0] * n
a = 0
for i in range(n):
    s = input()
    r = 0
    for j in range(n):
        if s[j] == 'C':
            r += 1
            c[j] += 1
    a += r * (r - 1) >> 1
for r in c:
    a += r * (r - 1) >> 1
print(a)
