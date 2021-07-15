a = input()
b = ['A', 'E', 'I', 'O', 'U', 'Y']
m = 1
c = 0
for i in range(len(a)):
    if a[i] in b:
        c = 0
    else:
        c += 1
    m = max(m, c + 1)
print(m)
