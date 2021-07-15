import sys
def input():
    return sys.stdin.readline().strip()

def calc(x,n):
    ans = 0
    for i,a in enumerate(x):
        ans += (2*i-n+1)*a
    return ans

n,m = list(map(int,input().split()))
x = tuple(map(int,input().split()))
y = tuple(map(int,input().split()))

print((calc(x,n)*calc(y,m)%(int(1e9+7))))

