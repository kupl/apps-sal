x = 0
n = int(input())
s = input()
l = [0]
for i in s:
    if i == 'I':
        x += 1
        l.append(x)
    else:
        x -= 1
        l.append(x)
print(max(l))
