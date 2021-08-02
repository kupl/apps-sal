a = int(input())
b = int(input())
n = a + b + 1
if(b is 0):
    for i in range(n):
        print(i + 1, end=' ')
elif(a is 0):
    for i in range(n):
        print(n - i, end=' ')
else:
    i = 1
    print(i, end=' ')
    i = i + b + 1
    while(i <= n):
        print(i, end=' ')
        i = i + 1
    ct, i = 1, 1 + b
    while(ct <= b):
        print(i, end=' ')
        i = i - 1
        ct = ct + 1
