n = int(input())
s = list(input())
max = x = 0
for i in s:
    if i == 'I':
        x += 1
    else:
        x -= 1
    if max < x:
        max = x
print(max)
