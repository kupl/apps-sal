a = int(input())
if a > 0:
    print(a)
elif int(str(a)[-1]) > int(str(a)[-2]):
    print(str(a)[:-1])
elif str(a)[:-2] + str(a)[-1] == '-0':
    print(0)
else:
    print(str(a)[:-2], str(a)[-1], sep='')
