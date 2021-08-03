n, t = map(int, input().split())
y = 10**5
for i in range(n):
    c, x = map(int, input().split())
    if x <= t:
        y = min(y, c)
if y != 10**5:
    print(y)
else:
    print("TLE")
