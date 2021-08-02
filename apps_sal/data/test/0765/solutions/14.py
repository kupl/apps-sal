n, m, r = list(map(int, input().split()))
o = 0
while(m < n):
    m *= r
    o += 1
print(o)
