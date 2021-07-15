n = int(input())
mylist = [0,0,0]
import math
for i in range(3):
    num = input()
    num = num.split()
    for j in range(len(num)):
        num[j] = int(num[j])
    mylist[i] = sum(num)
print(mylist[0] - mylist[1])
print(mylist[1] - mylist[2])

    
            

