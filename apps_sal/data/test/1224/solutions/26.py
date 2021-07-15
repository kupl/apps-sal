N = int(input())
b = 1
flag = 0
while 5**b<=N:
    x = N-5**b
    flag = 0
    a = 1
    while 3**a<=x:
        if 3**a==x:
            flag = 1
            break
        a += 1
    if flag==1:break
    b += 1
if flag==0:
    print(-1)
else:
    print(a,b)
