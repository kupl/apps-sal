d, t, s = map(int, input().split())

d = float(d)
t = float(t)
s = float(s)

if(d / s <= t):
    print("Yes")
else:
    print("No")
