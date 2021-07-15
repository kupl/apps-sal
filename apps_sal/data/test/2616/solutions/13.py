import math
######################################################
# ps template
def mi(): return map(int, input().split())
def ii(): return int(input())
def li(): return list(map(int, input().split()))
def si(): return input().split()

#######################################################
t = ii()
for _ in range(t):
    n = ii()
    a = li()
    ind = n-1
    for i in range(n):
        if a[i]>1:
            ind = i
            break
    if ind%2==0:
        print("First")
    else:
        print("Second")
