from sys import stdin as cin
from fractions import gcd

n,m = list(map(int,cin.readline().split()))
a=list(map(int,cin.readline().split()))
max_index=0
if a[0]%m==0:
    index = a[0]//m
else:
    index = a[0]//m+1
for i in range(n):
    if a[i]%m==0:
        temp = a[i]//m
    else:
        temp = a[i]//m+1
    if temp >= index :
        index = temp
        max_index = i
print(max_index+1)









