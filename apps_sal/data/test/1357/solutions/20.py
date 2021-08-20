(n, m) = map(int, input().split())
M = list(map(int, input().split()))
now = 1
time = 0
for i in M:
    if i >= now:
        time += i - now
    else:
        time += n - now + i
    now = i
print(time)
