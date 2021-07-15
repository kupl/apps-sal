#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

n,k = list(map(int, input().split()))
a = list(map(int, input().split()))

d = [0]*(n+1)

for i in range(n):
    d[a[i]] += 1

d.sort()

print((sum(d[:n-k+1])))

