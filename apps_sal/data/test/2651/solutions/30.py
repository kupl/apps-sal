import sys
input = sys.stdin.readline
n,m = map(int,input().split())
mod = 10**9+7
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
ans_x = 0
ans_y = 0
for i,xi in enumerate(x):
  ans_x += i*xi-(n-1-i)*xi
  ans_x %= mod
for j,yi in enumerate(y):
  ans_y += j*yi-(m-1-j)*yi
  ans_y %= mod
print(ans_x*ans_y%mod)
