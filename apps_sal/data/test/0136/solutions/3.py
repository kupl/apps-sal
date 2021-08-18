
import time


def nz(x):
    a = 0
    for i in range(len(x)):
        if x[i] == '0':
            a += 1
        else:
            break
    return x[a:]


a = list(input())
b = list(input())

start = time.time()

a = nz(a)
b = nz(b)

if len(a) == len(b):
    flag = True
    for i in range(len(a)):
        if a[i] < b[i]:
            print('<')
            flag = False
            break
        elif a[i] > b[i]:
            print('>')
            flag = False
            break
    if flag == True:
        print('=')
elif len(a) < len(b):
    print('<')
else:
    print('>')
finish = time.time()
