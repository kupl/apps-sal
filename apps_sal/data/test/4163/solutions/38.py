n = int(input())
a = []
b = []
for i in range(n):
    (x, y) = input().split(' ')
    a.append(x)
    b.append(y)
res = False
c = 0
for i in range(n):
    if a[i] == b[i]:
        if c == 2:
            res = True
            break
        c += 1
    else:
        c = 0
print('Yes' if res else 'No')
