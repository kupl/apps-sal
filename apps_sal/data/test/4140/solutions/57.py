import sys
import copy
import math
import itertools
import numpy as np
S = input()
#010101...との比較
cnt = [0,0]
for i in range(len(S)):
    if i%2==0 and int(S[i]) == 1:
        cnt[0]+=1
    elif i%2 == 1 and int(S[i]) == 0:
        cnt[0]+=1
    
    if i%2==0 and int(S[i]) == 0:
        cnt[1]+=1
    elif i%2 == 1 and int(S[i]) == 1:
        cnt[1]+=1
    
if cnt[0]<=cnt[1]:
    print(cnt[0])
else:
    print(cnt[1])
