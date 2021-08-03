d = input().split()
n = int(d[0])
k = int(d[1])
a = []
while n > 0:
    a.append(n % 10)
    n //= 10
a.reverse()


for i in range(len(a)):
    b = a[i:i + k + 1]
    for l in range(len(b)):
        if b[l] == max(b):
            j = l + i
            break
    if a[j] > a[i]:
        for x in range(j, i, -1):
            a[x], a[x - 1] = a[x - 1], a[x]
        k = k - (j - i)
s = ''
for i in range(len(a)):
    s += str(a[i])
print(s)
