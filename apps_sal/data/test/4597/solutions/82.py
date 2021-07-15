n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

mod = 10**9 + 7
p = 1
for i in range(1, n+1):
    p = (p*i) % mod
print(p)

