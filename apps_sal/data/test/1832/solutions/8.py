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
    n=int(input())
    a=list(map(int,input().split()))
    s="abcdefghijklmnopqrstuvwxyz"
    dict={}
    for i in range(25):
        dict[s[i]]=s[i+1]
    dict['z']='a'
    s="a"*200
    print(s)
    for i in range(n):
        p=s[0:a[i]]+dict[s[a[i]]]+s[a[i]+1:]
        s=p
        print(p)

