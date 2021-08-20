n = int(input())
c = input()
x = 0
for i in range(n):
    if c[i] == 'R':
        x += 1
y = 0
if x != 0:
    for j in range(x):
        if c[j] == 'W':
            y += 1
print(y)
