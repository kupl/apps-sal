x, n = map(int, input().split())
p = list(map(int,input().split()))
s = x
d = 1
while s in p:
    s = s - d
    d = int((abs(d)+1)*d/abs(d)*(-1))
print(s)
