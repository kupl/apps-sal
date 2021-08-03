a = int(input())
if(a // 10 == 0):
    print(a)
    return
k = 9
while(k < a):
    k = k * 10 + 9
if(k == a):
    print(k)
else:
    k //= 10
    k = int(str(a)[0] + str(k))
    i = len(str(k)) - 1
    z = k
    while(z > a):
        z = int(str(k)[0:i] + str(int(str(k)[i]) - 1) + str(k)[i + 1:len(str(k))])
        i -= 1
    print(z)
