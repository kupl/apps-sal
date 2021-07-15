d = input().split()
n = int(d[0]); x = int(d[1]); t = int(d[2])
a = n // x
if n % x != 0:
    a += 1
print(a * t)
