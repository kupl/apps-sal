s = input()
l = s.split(' ')
c = int(l[1])
n = int(l[0])
s = input()
l = s.split(' ')
b = []
for i in l:
    b.append(int(i))
m = 0
for i in range(len(b) - 1):
    if b[i] - b[i + 1] - c > m:
        m = b[i] - b[i + 1] - c
print(m)
