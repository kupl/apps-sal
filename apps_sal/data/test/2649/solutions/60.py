n = int(input())
# n = 2*10**5

min_u = float('inf')
max_u = -float('inf')
min_v = float('inf')
max_v = -float('inf')


for i in range(n):
    x, y = list(map(int, input().split()))
    # x, y = (10**9 , 10**9)
    u, v = (x+y, x-y)
    if u <= min_u:
        min_u = u
    if u >= max_u:
        max_u = u
    if v <= min_v:
        min_v = v
    if v >= max_v:
        max_v = v

print((max(max_u - min_u, max_v - min_v)))

