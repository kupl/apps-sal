'''
Created on ١٣‏/١٢‏/٢٠١٤

@author: mohamed265
'''
t = input().split()
for i in range(int(t[1])):
    print(int(t[0]) - i, end=' ')
for i in range(int(t[0]) - int(t[1])):
    print(i + 1, end=' ')
