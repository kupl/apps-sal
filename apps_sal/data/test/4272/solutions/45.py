import numpy as np

N=int(input())
S=input()
count=0
for i in range(N-2):
    if S[i] == 'A' and S[i+1]=='B' and S[i+2]=='C':
        count=count+1
print(count)
