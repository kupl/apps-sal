a = [0] + [int(i)for i in input().split()]
while a[1] * a[2] != 0:
    a = [a[0] + a[1] // a[2], a[2], a[1] % a[2]]
print(a[0])
