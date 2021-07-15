import sys, os.path
from collections import deque
from fractions import Fraction as f
def IO():
    if os.path.exists('input.txt'):
        sys.stdin = open('input.txt', 'r')
        sys.stdout = open('output.txt', 'w')
    else:
        input=sys.stdin.readline
        print=sys.stdout.write
def nextInt():
    return int(input())
def nextTuple():
    return [int(a) for a in input().split()]
def nextArray():
    return list(map(int, input().split()))
def nextLine():
    return input()
def nextStringArray():
    return list(input().split())
IO()

'''code starts here'''

t=int(input())
for _ in range(t):
    n,k,l=[int(x) for x in input().split()]
    a=list(map(int,input().split()))
    flag=0
    count=-1
    for i in range(n):
        if a[i]>l:
            flag=1
            break
    for i in range(n):
        if a[i]+k>l:
            if count==-1:
                count=k+(a[i]+k)-l
                continue
            count+=1
            count=count%(2*k)
            if count<=k:
                if a[i]+count>l:
                    flag=1
                    break
            else:
                now=k+(a[i]+k)-l
                count=max(count,now)
        else:
            count=-1
    if flag==1:
        print("No")
    else:
        print("Yes")
