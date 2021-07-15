n = int(input())
s = input()
c = 0

for i in s:
    if c == 0 and i == '-':
        pass
    elif i == '+':
        c += 1
    else:
        c -= 1
print(c)

