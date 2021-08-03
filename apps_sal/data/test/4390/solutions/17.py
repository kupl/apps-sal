MOD = 1000000007
MOD2 = 998244353
def ii(): return int(input())
def si(): return input()
def dgl(): return list(map(int, input()))
def f(): return map(int, input().split())
def il(): return list(map(int, input().split()))
def ls(): return list(input())


let = 'abcdefghijklmnopqrstuvwxyz'
for _ in range(ii()):
    a, b = f()
    x = (b - (a % b)) % b
    print(x)
