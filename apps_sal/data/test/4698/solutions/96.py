n = int(input())
t = list(map(int,input().split()))
s = sum(t)
m = int(input())
for i in range(m):
    p,x = map(int,input().split())
    print(s+(x-t[p-1]))
