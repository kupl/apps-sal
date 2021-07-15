# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
# TAIWAN NUMBER ONE!!!!!!!!!!!!!!!!!!!
from sys import stdin, stdout
import math

N = int(input())
s = input()
#N,M = [int(x) for x in stdin.readline().split()]
#arr = [int(x) for x in stdin.readline().split()]

room = [0]*10

for i in range(N):
    letter = s[i]
    
    if letter=='L':
        for j in range(10):
            if room[j]==0:
                room[j] = 1
                break
    elif letter=='R':
        for j in range(9,-1,-1):
            if room[j]==0:
                room[j] = 1
                break
            
    else:
        d = int(letter)
        room[d] = 0
        
print(*room,sep='')
