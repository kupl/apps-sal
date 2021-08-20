N = int(input())
flag = False
for i in range(10):
    if flag == True:
        continue
    if i != 0:
        one = N / i
        if one.is_integer() == True and one < 10:
            flag = True
if flag == True:
    print('Yes')
else:
    print('No')
