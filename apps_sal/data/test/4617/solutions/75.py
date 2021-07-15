import bisect,collections,copy,heapq,itertools,math,string
import sys
def I():
    #1 line 1 int
     return int(sys.stdin.readline().rstrip())
def LI():
    #1 line n int
     return list(map(int,sys.stdin.readline().rstrip().split()))
def S():
    #1 line 1 string
     return sys.stdin.readline().rstrip()
def LS():
    #1 line n strings
     return list(sys.stdin.readline().rstrip().split())

C1=S()
C2=S()

if C1[0]==C2[2] and C1[1]==C2[1] and C1[2]==C2[0]:
    print("YES")
else:
    print("NO")
