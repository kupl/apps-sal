from sys import stdin,stdout
import math 
from collections import Counter,deque
L=lambda:list(map(int, stdin.readline().strip().split()))
M=lambda:list(map(int, stdin.readline().strip().split()))
I=lambda:int(stdin.readline().strip())
IN=lambda:stdin.readline().strip()
C=lambda:stdin.readline().strip().split()
mod=1000000007
#Keymax = max(Tv, key=Tv.get)
def s(a):print(" ".join(list(map(str,a))))
#______________________-------------------------------_____________________#
#I_am_pavan
def solve():
    n,m,k=M()
    print(m*(m-1)//2)
    for i in range(1,m+1):
        for j in range(i+1,m+1):
            if k:
                print(j,i)
            else:print(i,j)
for i in range(1):
    solve()

