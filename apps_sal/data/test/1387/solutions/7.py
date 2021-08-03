n, m = input().split(' ')
n = int(n)
m = int(m)
seq = [1]
a = input()
line = a.split(' ')
c = 1
while c != n:
    c += int(line[c - 1])
    seq.append(c)
if m in seq:
    print("YES")
else:
    print("NO")
