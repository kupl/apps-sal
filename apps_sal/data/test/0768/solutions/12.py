# kitten
f, I, t = map(int, input().split())
l = []
for i in range(f):
    l.append(input())
a = 0
for i in range(I):
    c = 0
    for s in range(f):
        if l[s][i] == 'Y':
            c += 1
    if c >= t:
        a += 1
print(a)
