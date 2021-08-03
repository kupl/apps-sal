k = int(input())
if(str(k)[0] == '-'):
    st = "-0" + str(abs(k))
else:
    st = "0" + str(k)
a = int(st[:-1])
b = int(st[:-2] + str(k)[-1])
print(max(a, b, k))
