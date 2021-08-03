n = int(input())
x = 0
for i in range(n):
    line = input()
    if line == '++X' or line == 'X++':
        x += 1
    else:
        x -= 1
print(x)
