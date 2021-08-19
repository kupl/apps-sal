n = int(input())
d = dict()
for i in range(n):
    a = input().split()
    if a[0] not in d:
        d[a[0]] = []
    for j in range(2, len(a)):
        a[j] = a[j][::-1]
    d[a[0]] += a[2:]
print(len(d))
for x in d:
    a = d[x]
    a.sort(reverse=True)
    b = [a[0]]
    for i in range(1, len(a)):
        if a[i - 1][:len(a[i])] != a[i]:
            b += [a[i]]
    for i in range(len(b)):
        b[i] = b[i][::-1]
    print(x, len(b), *b)
