# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
from sys import stdin, stdout
import collections
 
Q = int(input())
 
#s = input()
#N = len(s)
#arr = [int(x) for x in stdin.readline().split()]
for i in range(Q):
    N,K = [int(x) for x in stdin.readline().split()]
    arr = [int(x) for x in stdin.readline().split()]
    
    odds = 0
    
    for i in range(N):
        if arr[i]%2==1:
            odds += 1
            
    if odds<K:
        print('NO')
        continue
    
    elif (odds-K)%2==1:
        print('NO')
        continue
    
    three = (odds-K)//2
    
    print('YES')
    odds = 0
    if K==1:
        print(N)
        continue
    
    for i in range(N):
        if arr[i]%2==1:
            odds += 1
        if three>0 and odds!=3:
            continue
        elif three>0 and odds==3:
            K -= 1
            print(i+1,end=' ')
            three -= 1
            odds = 0
        elif three==0 and odds==1:
            K -= 1
            print(i+1,end=' ')
            odds = 0
        if K==1:
            break
    print(N,end='\n')





