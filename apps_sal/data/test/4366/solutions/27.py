a,b = map(int,input().split())
t = a + b
if t >= 24:
    print(t - 24)
else:
    print(t)
