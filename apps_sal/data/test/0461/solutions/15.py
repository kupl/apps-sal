n = int(input())
a = int(input())
b = int(input())
c = int(input())
dist = 0
curr = 'r'
while n > 1:
    n -= 1
    if curr == 'e':
        if b < c:
            curr = 'r'
            dist += b
        else:
            curr = 'o'
            dist += c
    elif curr == 'o':
        if a < c:
            curr = 'r'
            dist += a
        else:
            curr = 'e'
            dist += c
    elif a < b:
        curr = 'o'
        dist += a
    else:
        curr = 'e'
        dist += b
print(dist)
