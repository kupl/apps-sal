n, t = list(map(int, input().split()))
l = list(map(int, input().split()))
s = 0
z = 0
for i in l:
    if z - i > 0:
        s += i + t - z
    else:
        s += t
    z = i + t
print(s)
