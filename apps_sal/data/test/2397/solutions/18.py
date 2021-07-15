from sys import stdin,stdout
from itertools import combinations
from collections import defaultdict,OrderedDict
import math
import heapq

def listIn():
    return list((list(map(int,stdin.readline().strip().split()))))

def stringListIn():
    return([x for x in stdin.readline().split()])
    
def intIn():
    return (int(stdin.readline()))

def stringIn():
    return (stdin.readline().strip())

def __starting_point():
    n,k=listIn()
    a=listIn()
    arr=[a[0]]+[0]*(n-1)
    
    for i in range(1,n):
        arr[i]=arr[i-1]+a[i]
    
    #print(*arr)
    max_cost=arr[n-1]*k
    
    b=sorted(arr[:n-1])
    for i in range(k-1):
        max_cost-=b[i]
    
    print(max_cost)
        
    

__starting_point()
