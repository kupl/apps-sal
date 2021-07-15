import sys
pin=sys.stdin.readline
#わからんわこれ
def main():
  N,K=map(int,pin().split())
  A=list(map(int,pin().split()))
  print((N-2)//(K-1)+1)
  return
main()
