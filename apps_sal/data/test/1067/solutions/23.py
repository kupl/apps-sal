import sys
input = sys.stdin.readline

def getInt(): return int(input())
def getVars(): return list(map(int, input().split()))
def getArr(): return list(map(int, input().split()))
def getStr(): return input().strip()
## -------------------------------

N = getInt()
A = getArr()

res = 0
k = 1
for i in range(N):
    res += abs(abs(A[i]) - 1)
    if A[i] == 0:
        k = 0
    if A[i] <= -1:
        k *= -1
if k >= 0:
    print(res)
else:
    print(res + 2)

