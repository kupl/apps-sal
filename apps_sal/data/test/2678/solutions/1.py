# cook your dish here
from operator import itemgetter
n=int(input())
array=[]
for _ in range(n):
    array.append(list(map(int, input().split())))
array.sort(key=itemgetter(1))
array.sort(key=itemgetter(0))
appo=array[0]
counter=1
for i in range(1,n):
    if appo[1]<array[i][0]:
        counter+=1
        appo=array[i]
    else:
        appo[0] = array[i][0]
        appo[1] = min(appo[1], array[i][1])
print(counter)
