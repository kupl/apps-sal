n = int(input())
s = input()
x = 0
l = [0]
for a in s:
    if a == 'I':
        x = x + 1
        l.append(x)
    else:
        x = x - 1
        l.append(x)
print(max(l))
