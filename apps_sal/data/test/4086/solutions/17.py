d = set()

n = int(input())
a = [int(x) for x in input().split()]
b = []
for i in range(n - 1, -1, -1):
    if a[i] in d:
        continue
    b.append(a[i])
    d.add(a[i])
b.reverse()

print(len(b))
for x in b:
    print(x, end=' ')
