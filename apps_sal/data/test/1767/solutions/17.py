input()
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
a1 = a[0]
for i in a[1:]:
    a1 = a1 | i
b1 = b[0]
for i in b[1:]:
    b1 = b1 | i

print(a1 + b1)
