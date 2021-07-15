a, b = list(map(int,input().split()))
l = 0
r = a + 1
while r - l > 1:
    m = (r + l) // 2
    #print(l, r)
    if m * (m + 1) // 2 - (a - m) > b:
        r = m
    else:
        l = m
print(a - l)
