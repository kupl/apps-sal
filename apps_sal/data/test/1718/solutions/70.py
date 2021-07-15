import sys
def MI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N,K = MI()
A = LI()

print(((N-1+K-2)//(K-1)))

