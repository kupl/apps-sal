n = int(input())
x = 0
b = []
s = input()
for S in s:
    if S == 'I':
        x += 1
        b.append(x)
    else:
        x -= 1
        b.append(x)
print(max(max(b), 0))
