import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())
def NIJIGEN(H): return [list(input()) for i in range(H)]
mod=1000000007
N=INT()
L=LIST()
if N%2==0:
  A=range(1,N,2)
  B=range(1,N,2)
else:
  A=range(0,N,2)
  B=range(2,N,2)
A,B=list(A),list(B)
A=A+B
if sorted(A)==sorted(L):
  print(pow(2,N//2,mod))
else:
  print(0)
