f, i, t = input().split()
f = int(f)
i = int(i)
t = int(t)
a = [0] * i
m = [0] * i

for v in range(f):
    p = input()
    for w in range(i):
        if p[w] == 'Y':
            a[w] += 1
            if a[w] >= t:
                m[w] = 1
print(sum(m))  # kitten
