n = int(input())
s = str(input())
x = 0
a = 0
for i in s:
    if i == 'I':
        x += 1
        if x > a:
            a = x
    else:
        x -= 1
print(a)
