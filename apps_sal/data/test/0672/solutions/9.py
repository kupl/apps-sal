a = input().split(' ')
x1 = int(a[0])
y1 = int(a[1])
a1 = x1 - y1
if x1 == y1:
    print('infinity')
else:
    i = 1
    counter = 0
    while i ** 2 <= a1:
        counter += (a1 % i == 0 and i > y1) + (a1 % i == 0 and a1 // i > y1 and (i != a1 // i))
        i += 1
    print(counter)
