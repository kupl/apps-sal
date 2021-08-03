n = int(input())
a = 0
for i in range(n):
    v, c = input().split()
    v = float(v)
    if c == "JPY":
        a += v
    else:
        a += v * 380000.0
print(a)
