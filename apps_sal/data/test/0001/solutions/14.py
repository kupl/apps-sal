x = input()
sum = 0
for i in x:
    temp = int(i)
    sum += temp

xlen = len(x)
one = int(x[0])
try:
    two = int(x[1])
except:
    two = 0

if (two == 9):
    count = 1
    for i in range(1, xlen):
        z = int(x[i])
        if (z == 9):
            count = i
        else:
            break
    answ = x[0:count] + "8" + ("9" * (xlen - count - 1))
elif (one == 1):
    answ = '9' * (xlen - 1)
else:
    answ = str((one - 1)) + ("9" * (xlen - 1))

answ = str(answ)
sumansw = 0
for i in answ:
    temp = int(i)
    sumansw += temp

if (sum >= sumansw):
    print(x)
else:
    print(answ)
