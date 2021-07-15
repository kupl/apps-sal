'''
Created on Oct 5, 2014

@author: Ismael
'''
from _collections import defaultdict

def DFexplo(dictAdj,start):
    explored = {start}
    lifo = [start]
    while(len(lifo)>0):
        node = lifo.pop()
        for child in dictAdj[node]:
            if(child not in explored):
                explored.add(child)
                lifo.append(child)
    return explored

def solve(dictAdj):
    #print(dictAdj)
    for i in range(len(H)):
        for j in range(len(V)):
            nodesReachable = DFexplo(dictAdj,(i,j))
            if(len(nodesReachable) < n*m-1):
                return False
    return True

def isNode(i,j):
    return 0 <= i < n and 0 <= j < m

def buildGraph(H,V):
    dictAdj = defaultdict(list)
    for i in range(len(H)):
        for j in range(len(V)):
            if(isNode(i,j-1) and H[i]=='<'):
                dictAdj[(i,j)].append((i,j-1))
            if(isNode(i,j+1) and H[i]=='>'):
                dictAdj[(i,j)].append((i,j+1))
            if(isNode(i-1,j) and V[j]=='^'):
                dictAdj[(i,j)].append((i-1,j))
            if(isNode(i+1,j) and V[j]=='v'):
                dictAdj[(i,j)].append((i+1,j))
    return dictAdj

n,m = map(int,input().split())
H = input()
V = input()
dictAdj = buildGraph(H,V)
if(solve(dictAdj)):
    print("YES")
else:
    print("NO")
