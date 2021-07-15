import collections
import math
from itertools import permutations as p

for t in range(int(input())):
    n=int(input())
    s=input()
    stack=[]
    for i in s:
        if i=='1':
            if stack and stack[-1]=='0':
                stack.pop()
        else:
            if stack and stack[-1]=='1':
                stack.pop()
        stack.append(i)
    print(len(stack)//2)
