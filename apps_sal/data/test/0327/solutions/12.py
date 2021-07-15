import sys
sys.setrecursionlimit(1000000)
read = sys.stdin.readline

N, K = map(int, read().split())
if K == 1:
    print(N)
    return
allOne = 1
while((allOne<<1) <= N):
    allOne <<= 1
allOne<<=1
allOne -= 1
print(allOne)
