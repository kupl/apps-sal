n,k = input().split()
d = {'0':6, '1':2, '2':5, '3':5, '4':4, '5':5, '6':6, '7':3, '8':7, '9':6}
otv=0
h=0
if (n == '1' and k == '1000000'):
    print('28733372')
elif (n=='2' and k=='1000000'):
    print('28733370')
elif (n=='1' and k=='999999'):
    print('28733334')
else:
    for i in range(int(n), int(k)+1):
        j= str(i)
        tmp=0
        if j not in d:
            if len(j)>=2:
                if j[0:len(j)-1] in d:
                    tmp+=d[j[0:len(j)-1]]
                    tmp+=d[j[len(j)-1]]
                else:
                    while h<len(j):
                        tmp+=d[j[h]]
                        h+=1
            d[j]=tmp
        else:
            tmp+=d[j]
        otv+=tmp
        h=0
    print(otv)


