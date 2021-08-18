"""
Created on Thu Nov 30 12:11:39 2017

@author: vishal
"""

n = int(input())
a = int(input())
b = int(input())

if(4 * a + 2 * b <= n):
    print(1)
elif(2 * a + b <= n or a + 2 * b <= n and 3 * a <= n):
    print(2)
elif(a + b <= n and 2 * a <= n or 2 * b <= n and 2 * a <= n or 4 * a <= n):
    print(3)
elif(2 * a <= n or a + b <= n):
    print(4)
elif(2 * b <= n):
    print(5)
else:
    print(6)
