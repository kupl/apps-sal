L = list(input())
for i in range(len(L)):
    a = L[i]
    if int(a) < 5:
        continue
    b = 9 - int(a)
    L[i] = str(b)
if L[0] == '0':
    L[0] = '9'
print("".join(L))
