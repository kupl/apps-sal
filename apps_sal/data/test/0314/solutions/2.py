N, K = list(map(int, input().split()))
a = [int(i) for i in input().split()]

store = 0
s = 0
for day in range(N):
    store += a[day]
    x = min(8, store)
    s += x
    store -= x
    if s >= K:
        break

if s >= K:
    print(day + 1)
else:
    print(-1)
