(t, s, q) = list(map(int, input().split()))
r = 1
while t > s * q:
    s *= q
    r += 1
print(r)
