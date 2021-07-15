'''
Created on 2019. 9. 21.

@author: kkhh88
'''
#q = int(input())
#x, y = map(int,input().split(' '))
#print (' '.join(list(map(str, s))))

q = int(input())

for i in range(q):
    x, y = list(map(int,input().split(' ')))
    
    if x >= y:
        print("YES")
        continue;

    while 1:

        
        if x % 2 == 0:
            x = (x * 3) // 2
        else:
            x = ((x - 1) * 3) // 2

        if x >= y:
            print("YES")
            break

        if x <= 3:
            print("NO")
            break

        

