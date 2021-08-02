d, t, s = map(int, input().split())
# d=distance t=time s=speed per minute

time = d / s

if time > t:
    print("No")
else:
    print("Yes")
