a = int(input())
b = 0
flag = False
while True:
    a += 1
    b += 1
    for i in range(len(str(a))):
        if str(a)[i] == '8':
            flag = True
    if flag: break
print(b)
