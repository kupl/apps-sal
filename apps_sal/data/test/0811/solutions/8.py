a,b = list(map(int, input().split()))
c = a
d = 0
s = 0
while c:
    s += c
    d += c
    c = d // b
    d %= b
print(s)


