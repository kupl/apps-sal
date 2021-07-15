'''
Created on 2020/10/01

@author: harurun
'''
import sys
pin=sys.stdin.readline

def main():
  N=int(pin())
  su=0
  S=[]
  for i in range(N):
    s=int(pin())
    S.append(s)
    su+=s
  if su%10!=0:
    print(su)
    return
  S.sort()
  for i in S:
    if (su-i)%10!=0:
      print(su-i)
      return
  print(0)
  return
main()
