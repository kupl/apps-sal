n = int(input())
t,a = map(int, input().split())
al = list(map(int, input().split()))

temp = 10**6
res = 0
for i in range(n):
    dt = abs((t - al[i]*0.006)-a)
    if temp >= dt:
        temp = dt
        res = i+1

print(res)
