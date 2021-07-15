#Bhargey Mehta (Sophomore)
#DA-IICT, Gandhinagar
import sys, math, queue, bisect
#sys.stdin = open("input.txt", "r")
MOD = 10**9+7
sys.setrecursionlimit(1000000)

def mxr(x):
    n = len(x)
    ans = [n for i in range(n)]
    s = []
    for i in range(n):
        while len(s) > 0 and x[s[-1]] < x[i]:
            ans[s.pop()] = i
        s.append(i)
    return ans

def mnr(x):
    n = len(x)
    ans = [n for i in range(n)]
    s = []
    for i in range(n):
        while len(s) > 0 and x[s[-1]] > x[i]:
            ans[s.pop()] = i
        s.append(i)
    return ans

def mxl(x):
    ans = [-1 for i in range(n)]
    s = []
    for i in range(n-1, -1, -1):
        while len(s) > 0 and x[s[-1]] <= x[i]:
            ans[s.pop()] = i
        s.append(i)
    return ans

def mnl(x):
    ans = [-1 for i in range(n)]
    s = []
    for i in range(n-1, -1, -1):
        while len(s) > 0 and x[s[-1]] >= x[i]:
            ans[s.pop()] = i
        s.append(i)
    return ans

n = int(input())
a = list(map(int, input().split()))
maxl = mxl(a)
minl = mnl(a)
maxr = mxr(a)
minr = mnr(a)
ans = 0
for i in range(n):
    mxrng = (maxr[i]-i)*(i-maxl[i])
    mnrng = (minr[i]-i)*(i-minl[i])
    ans += a[i]*(mxrng-mnrng)
print(ans)
