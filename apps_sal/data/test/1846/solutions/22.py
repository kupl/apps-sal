import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
MOD = 1000000007
def ii(): return int(input())
def si(): return input()
def dgl(): return list(map(int, input()))
def f(): return list(map(int, input().split()))
def il(): return list(map(int, input().split()))
def ls(): return list(input())


n = ii()
l = il()
lf = [0] * n
lf[0] = 1if l[0] >= 0else 0
lb = [0] * n
lb[-1] = 1if l[-1] <= 0else 0
for i in range(1, n):
    if l[i] >= 0:
        lf[i] = lf[i - 1] + 1
    else:
        lf[i] = lf[i - 1]
for i in range(n - 2, -1, -1):
    if l[i] <= 0:
        lb[i] = lb[i + 1] + 1
    else:
        lb[i] = lb[i + 1]
mn = 10**10
for i in range(n - 1):
    mn = min(mn, lf[i] + lb[i + 1])
print(mn)
