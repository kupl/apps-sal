arr = input().split()
p = int(arr[0])
q = int(arr[1])
a = int(arr[2])
b = int(arr[3])
flag = 0
if a <= b:
    a = b + 1
x = b
y = a
while a <= p:
    b = x
    while b < a and b <= q:
        flag += 1
        b += 1
    a += 1
print(str(flag))
a = y
b = x
while a <= p:
    b = x
    while b < a and b <= q:
        flag += 1
        print(str(a) + ' ' + str(b))
        b += 1
    a += 1
