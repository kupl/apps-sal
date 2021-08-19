n = int(input())
a = int(input())
b = int(input())
c = int(input())
count = 1
length = 0
x = 1
while count < n:
    count += 1
    if x == 1:
        if a < b:
            x = 2
            length += a
        else:
            x = 3
            length += b
    elif x == 2:
        if a < c:
            x = 1
            length += a
        else:
            x = 3
            length += c
    elif b < c:
        x = 1
        length += b
    else:
        x = 2
        length += c
print(length)
