n = int(input())
a = 0
x = 9999
for _ in range(n):
    v = int(input())
    a += v
    if v % 10 != 0:
        x = min(x, v)
if a % 10 != 0:
    print(a)
elif x == 9999:
    print(0)
else:
    print(a - x)
