def isUnique(num):
    string=str(num)
    d={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for i in string:
        if d[i]==0:
            d[i]=1
        elif d[i]==1:
            return 0
    return 1

string=input()
num=int(string)
while 1:
    num+=1
    if isUnique(num):break
print(num)
