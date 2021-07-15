n = int(input())
t = list(map(int,input().split()))
m = int(input())
for i in range(m):
    a,b = map(int,input().split())
    T = sum(t) - t[a-1] + b
    print(T)
