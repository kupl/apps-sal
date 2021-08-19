input()
x = input()
a = 1
for i in range(len(x)):
    if x[i] == '0':
        break
    else:
        a += 1
    if i == len(x) - 1:
        a -= 1
print(a)
