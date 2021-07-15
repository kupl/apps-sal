from math import *
def main():
   a, b=list(map(int, input().split()))
   n=int(input())
   T=10**10
   for loop in range(n):
      x, y, v=list(map(int, input().split()))
      d=sqrt((a-x)**2+(b-y)**2)
      t=d/v
      T=min(t, T)
   print(T)
main()

