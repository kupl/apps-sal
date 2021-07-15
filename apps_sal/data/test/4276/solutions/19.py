n,t = map(int, input().split())

res = 10000

for i in range(n):
    a,b = map(int, input().split())
    if b <= t:
        res = min(res,a)

if res ==10000:
    print("TLE")
else:
    print(res)
