'''
Created on Feb 13, 2015

@author: mohamed265
'''
a1 = input()
a2 = input()
slon = 0
for i in range(ord('a'), ord('z') + 1):
    x = chr(i)
    count1 = a1.count(x)
    count2 = a2.count(x)
    if count1 == 0 and count2 != 0:
        print(-1)
        return
    else:
        if count1 >= count2:
            slon += count2
        else:
            slon += count1
print(slon)
