import sys
from math import sqrt
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

n,m = map(int,input().split())
a = list(map(int,input().split()))
size = 2 * 2**n # 8
segmentTree = [-1]*size # 1~7 
levels = [-1]*size

idx = 0
#initialize 
for i in range(int(size/2),size):
    segmentTree[i] = a[idx]
    levels[i] = 1
    idx+=1

#build segment tree
for i in range(2**n-1,0,-1): # 3,2,1
    left = 2*i; right = 2*i+1
    levels[i] = levels[2*i]+1
    if levels[i] % 2 == 0:
        segmentTree[i] = segmentTree[left] | segmentTree[right]
    else:
        segmentTree[i] = segmentTree[left] ^ segmentTree[right]

#update segment tree
for t in range(m):
    p,b = map(int,input().split())
    segmentTree[2**n+p-1] = b
    i = 2**n+p-1
    while i != 1:
        parent = int(i/2)
        left = parent*2; right = parent*2+1
        if levels[parent] % 2 == 0:
            segmentTree[parent] = segmentTree[left] | segmentTree[right]
        else:
            segmentTree[parent] = segmentTree[left] ^ segmentTree[right]
        i = parent
    print(segmentTree[1])
