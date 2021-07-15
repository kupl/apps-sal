import sys
def MI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N,M = MI()
a = LI()

count = 0  # 順送りボタンだけを用いたときのボタンを押す回数
X = [0]*(2*M+1)
Y = [0]*(2*M+1)
# (X[0]+…+X[i])*i+(Y[0]+…+Y[i]) = お気に入りボタンをiに設定した時に、ボタンの押す回数を何回節約できるか

for i in range(N-1):
    a0,a1 = a[i],a[i+1]
    count += (a1-a0) % M
    if a0 > a1:
        a1 += M
    if a0 == a1:
        continue
    X[a0+2] += 1
    X[a1+1] -= 1
    Y[a0+2] -= a0+1
    Y[a1+1] += a0+1

from itertools import accumulate

X = list(accumulate(X))
Y = list(accumulate(Y))

A = [0]*(M+1)
for i in range(1,M+1):
    A[i] = (X[i]*i+Y[i]) + (X[i+M]*(i+M)+Y[i+M])

print((count-max(A)))

