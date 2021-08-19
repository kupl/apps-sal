a = ['1', '2', '3']
(x, y) = input().split()
for i in range(3):
    if a[i] != x and a[i] != y:
        z = a[i]
print(z)
