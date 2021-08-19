(N, T) = map(int, input().split())
time = list(map(int, input().split())) + [float('inf')]
now = 0
prev = 0
ans = 0
for t in time:
    if t - prev >= T:
        ans += T
    else:
        ans += t - prev
    prev = t
print(ans)
