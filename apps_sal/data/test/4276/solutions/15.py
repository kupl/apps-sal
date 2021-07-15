n, t = map(int, input().split())

c = []

for i in range(0,n):
    c_i, t_i = map(int, input().split())

    if t_i <= t:
        c.append(c_i)

if len(c) > 0:
    print(min(c))
else:
    print("TLE")
