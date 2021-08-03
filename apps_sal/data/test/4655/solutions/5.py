mod = 1000000007
def ii(): return int(input())
def si(): return input()
def dgl(): return list(map(int, input()))
def f(): return map(int, input().split())
def il(): return list(map(int, input().split()))
def ls(): return list(input())


n = ii()
for i in range(n):
    a, b, c = f()
    print((a + b + c) // 2)
