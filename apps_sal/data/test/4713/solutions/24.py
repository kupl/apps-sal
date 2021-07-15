n = int(input())
s = str(input())
x = 0
maximum = 0

for i in range(n):
    if s[i] == 'I':
        x += 1
    elif s[i] == 'D':
        x -= 1
    maximum = max(maximum, x)

print(maximum)
