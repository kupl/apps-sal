a, ta = list(map(int, input().split()))
b, tb = list(map(int, input().split()))
h,m = list(map(int, input().split(":")))
d = 60*h+m
c = 300
r = 0
while c <= d - tb:
    c += b
while c < min(24*60,d + ta):
    c += b
    r += 1
print(r)

