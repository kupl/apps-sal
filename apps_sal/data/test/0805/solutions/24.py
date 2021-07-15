n = int(input())
Al_r = input()
Al = int(Al_r.split(' ')[0])
Ar = int(Al_r.split(' ')[1])
Al_rList = list(range(Al,Ar))
for i in range(n-1):
    l_r = input()
    l = int(l_r.split(' ')[0])
    r = int(l_r.split(' ')[1])
    l_rList = list(range(l, r))
    for i in l_rList:
        if i in Al_rList:
            Al_rList.remove(i)
print(len(Al_rList))
