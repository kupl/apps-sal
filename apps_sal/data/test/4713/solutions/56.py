n = int(input())
s = input()
x = 0
y = 0
for i in range(n):
    if s[i] == 'I':
        x += 1
        if x > y:
            y = x
    else:
        x -= 1
print(y)
