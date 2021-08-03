n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
count = 1
p = a[0]
num = 0
if n == 1:
    print(1)
else:
    for i in a[1:]:
        if i != p:
            p = i
            count += 1
        else:
            if num < count:
                num = count
            count = 1
    else:
        if num < count:
            num = count
    print(num)
