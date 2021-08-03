s = input()
k1 = 0
k0 = 0
for i in s:
    if i == '0':
        k0 += 1
    else:
        break
s = s[k0:]
k0 = 0
for i in s:
    if i == '0':
        k0 += 1
    else:
        k1 += 1
if k1 >= 1 and k0 >= 6:
    print("yes")
else:
    print("no")
