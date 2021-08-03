n = int(input())
a = dict()
for i in ['S', 'XS', 'XXS', 'XXXS', 'M', 'L', 'XL', 'XXL', 'XXXL']:
    a[i] = 0
for _ in ' ' * n:
    a[input()] += 1
for _ in ' ' * n:
    a[input()] -= 1
s = 0
for i in a:
    s += abs(a[i])
print(s // 2)
