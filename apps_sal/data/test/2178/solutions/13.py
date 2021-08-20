n = int(input())
a = input().split()
c = []
d = set()
for i in range(n):
    c.append(int(a[i]))
b = input().split()
index = 0
count = 0
stri = ''
for i in range(n):
    if int(b[i]) not in d:
        while c[index] != int(b[i]):
            d.add(c[index])
            index += 1
            count += 1
        d.add(c[index])
        index += 1
        count += 1
    if i == n - 1:
        stri += str(count)
    else:
        stri += str(count) + ' '
    count = 0
print(stri)
