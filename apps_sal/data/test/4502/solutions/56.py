n = int(input())
a = list(map(int, input().split()))

b = []
if n % 2 == 1:
    for i in a[n - 1:0:-2]:
        b.append("{0}".format(i))
    b.append(str(a[0]))
    for i in a[1:n:2]:
        b.append("{0}".format(i))

if n % 2 == 0:
    for i in a[n - 1:0:-2]:
        b.append("{0}".format(i))
    for i in a[0:n:2]:
        b.append("{0}".format(i))

print((' '.join(b)))
