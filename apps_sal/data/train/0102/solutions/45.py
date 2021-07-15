n = int(input())
for i in range(n):
    k = int(input())
    l = len(str(k))
    s = 9*(l-1)
    for i in range(9):
        if int(str(i+1)*l)>k:
            break
        s+=1
    print(s)

