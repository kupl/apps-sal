import sys
sys.setrecursionlimit(10**9)

MOD = 998244353
N = int(input())
robo = list(list(map(int,input().split()))for i in range(N))
robo.sort()
child = [[]for i in range(N+1)]
stack = [] # 有効、名前

for i in range(N):
    x,d = robo[i]
    while stack and stack[-1][0] <= x:
        stack.pop()
    if stack:
        child[stack[-1][1]].append(i+1)
    else:
        child[0].append(i+1)
    stack.append([x+d,i+1])

def func(x):
    hoge = 1
    for i in child[x]:
        hoge *= func(i)
        hoge %= MOD
    return (hoge + 1) % MOD

print((func(0)-1))

