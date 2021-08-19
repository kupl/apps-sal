n = int(input())
(a, b) = ([], [])
for i in range(n):
    a.append(input())
for i in range(n):
    b.append(input())
C = ['S', 'M', 'L', 'XL', 'XXL', 'XXXL', 'XS', 'XXS', 'XXXS']
d = []
for s in C:
    if a.count(s) - b.count(s) < 0:
        d.append(-(a.count(s) - b.count(s)))
print(sum(d))
