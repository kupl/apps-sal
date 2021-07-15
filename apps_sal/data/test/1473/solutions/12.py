'''
Created on ٢٧‏/١١‏/٢٠١٤

@author: mohamed265
'''
 
first = set()
second = set()
map = {}
n = int(input())
for i in range(n):
    temp = input().split()
    first.add(int(temp[0]))
    second.add(int(temp[1]))
    map[int(temp[0])] = int(temp[1])
    

# print(first)
# print(second)
# print(map)

temp = 0
res = [temp for x in range(n + 10)]
j = 2 
temp = 0

while temp in map.keys() :
    if  j > n + 1:
        break
    temp = map[temp]
    res[j] = temp
    j += 2
    
# print(res)
x = first - second
temp = int(x.pop())
j = 1

while temp != 0:
    res[j] = temp
    j += 2
    try:
        temp = map[temp]
    except:
        break
    
 
for i,  x  in  enumerate(res):
    if  i < n + 1:
        if  i != 0:   
            print(x , end=' ')
    
    
    
    

