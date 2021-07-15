li = list(input())
n = 0
for i in li:
    if i == '+':
        n += 1
    elif i == '-':
        n -= 1

print(n)
