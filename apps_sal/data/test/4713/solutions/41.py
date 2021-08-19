n = int(input())
s = input()
m = 0
x = 0
for w in s:
    if w == 'I':
        x += 1
    else:
        x -= 1
    if x > m:
        m = x
print(m)
