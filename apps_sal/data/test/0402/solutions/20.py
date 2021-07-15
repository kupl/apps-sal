'''
Created on 30 dec. 2016

@author: Moldovan
'''
from sys import stdout

n,k=input().split()
n = int(n)
k = int(k)
problems = 0
total = 60*4 - k
for i in range(n):
    if total >= 5*(i+1):
        problems = problems +1
        total = total - 5*(i+1)
        
print(problems) 

