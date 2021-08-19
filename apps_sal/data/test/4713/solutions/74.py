N = int(input())
S = str(input())
x = 0
L = [x]
for i in S:
    if i == 'I':
        x += 1
    if i == 'D':
        x -= 1
    L.append(x)
print(max(L))
