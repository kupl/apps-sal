a = input()
b = input()

A = len(a)
B = len(b)
d = B - A + 1

l = [-1] * A

count = 0

for i in range(d):
    if b[i] == '1':
        count += 1

l[0] = count
c = 0

for i in range(d, B):
    if b[i] == '1':
        count += 1
    if b[c] == '1':
        count -= 1
    c += 1
    l[c] = count

net = 0

for i in range(A):
    if a[i] == '0':
        net += l[i]
    else:
        net += d - l[i]

print(net)
