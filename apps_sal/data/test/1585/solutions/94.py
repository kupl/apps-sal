'''
Created on 2020/10/02

@author: harurun
'''
import sys
pin=sys.stdin.readline

def main():
  x,y=map(int,pin().split())
  cnt=0
  while x<=y:
    x*=2
    cnt+=1
  print(cnt)
  return
main()
