a = int(input())
b = input()
c = 0
d = [0]
for i in b:
    if i == 'I':
        c += 1
        d.append(c)
    elif i == 'D':
        c -= 1
        d.append(c)
print(max(d))
