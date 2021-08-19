n = int(input())
m = n % 2
o = n // 2
if m == 1:
    print(o * (o + 1))
else:
    print(o * o)
