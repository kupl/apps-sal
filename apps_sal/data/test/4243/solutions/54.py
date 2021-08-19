x = int(input())
k = 0
s = 0
if x // 500 > 0:
    k = x // 500
    s += k * 1000
    x = x - k * 500
if x // 5 > 0:
    k = x // 5
    s += k * 5
    x = x - k * 5
print(s)
