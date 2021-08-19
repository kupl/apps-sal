"""
Created on ٠١\u200f/١٢\u200f/٢٠١٤

@author: mohamed265
"""
n = int(input())
slon = 0
temp = 1
j = 2
while n >= temp:
    slon = slon + 1
    n -= temp
    temp += j
    j = j + 1
print(slon)
