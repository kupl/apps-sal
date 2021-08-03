n = int(input()) - 1
a = int(input())
b = int(input())
c = int(input())
result = 0
cur = 'k'
while n > 0:
    if cur == 'k':
        if a < b:
            cur = 's'
            result += a
        else:
            cur = 'i'
            result += b
    elif cur == 's':
        if a < c:
            cur = 'k'
            result += a
        else:
            cur = 'i'
            result += c
    else:
        if b < c:
            cur = 'k'
            result += b
        else:
            cur = 's'
            result += c
    n -= 1
print(result)
