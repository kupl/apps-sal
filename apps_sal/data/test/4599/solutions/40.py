N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
Alice = 0
Bob = 0
flag=True
for i in a:
    if flag==True:
        Alice += i
        flag = False
    else:
        Bob += i
        flag = True
print((Alice-Bob))

