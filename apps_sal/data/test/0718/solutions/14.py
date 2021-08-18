def f(a):
    flag = False
    for i in str(a):
        if (i == "8"):
            flag = True
    return flag


a = int(input())
d = 1
while not f(a + d):
    d += 1
print(d)
