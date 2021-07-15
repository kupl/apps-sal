x = int(input())
if x < 10:
    print(x)
elif x == int(str(x)[0] + '9'*(len(str(x))-1)):
    print(x)
else:
    a = str(x)[0] + '9' * (len(str(x)) - 1)
    a = list(a)
    for i in range(len(a) - 1, -1, -1):
        k = a[i]
        a[i] = str(int(a[i]) - 1)
        if x >= int(''.join(a)):
            print(int(''.join(a)))
            break
        a[i] = k

