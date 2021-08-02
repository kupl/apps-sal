N = int(input())
l = 0
r = 10**100
while(r - l > 1):
    m = (r + l) // 2
    if m * (m + 1) <= 2 * (N + 1):
        l = m
    else:
        r = m
print((N - l + 1))
