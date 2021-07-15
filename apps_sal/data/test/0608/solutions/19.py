n = int(input())
m = str(input())
m += ' '
k = 0
x = []
stri = ''
for i in m:
    if i != ' ':
        stri += i
    elif i == ' ':
        x.append(stri)
        stri = ''
k = 0
b = 0
for i in range(n):
    x[i] = int(x[i], 10)
    if x[i] > 3:
        k += 1
    else:
        k = 0
    if k == 3:
        k = 0
        b += 1
print(b)
