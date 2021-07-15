from heapq import *
x,y,z,k = map(int,input().split())
A,B,C = [list(map(int,input().split())) for n in range(3)]
D = nlargest(k,(a+b for a in A for b in B))
E = nlargest(k,(d+c for d in D for c in C))
print("\n".join(map(str,E)))
