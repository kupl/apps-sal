n = int(input())
w = []
for _ in range(n):
    w.append(input())
a = ''
for i in range(n):
    for j in range(i):
        if w[i] == w[j]:
            print('No')
            return
for j in w:
    b = [i for i in j]
    if j != w[0] and a != b[0]:
        print('No')
        return
    a = b[-1]
print('Yes')
