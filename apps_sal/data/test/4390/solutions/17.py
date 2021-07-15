MOD = 1000000007
MOD2 = 998244353
ii = lambda: int(input())
si = lambda: input()
dgl = lambda: list(map(int, input()))
f = lambda: map(int, input().split())
il = lambda: list(map(int, input().split()))
ls = lambda: list(input())
let = 'abcdefghijklmnopqrstuvwxyz'
for _ in range(ii()):
    a,b=f()
    x=(b-(a%b))%b
    print(x)
