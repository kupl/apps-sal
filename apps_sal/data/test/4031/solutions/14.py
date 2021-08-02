n = int(input())
a = []
for i in range(n):
    a.append(input())
b = [a[0]]
for j in range(1, n):
    b.append(a[j])
    c = len(b) - 1
    while c != 0 and b[c - 1] not in b[c]:
        b[c - 1], b[c] = b[c], b[c - 1]
        c -= 1
flag = True
for i in range(1, n):
    if b[i - 1] not in b[i]:
        flag = False

if flag:
    print("YES")
    for i in b:
        print(i)
else:
    print("NO")
