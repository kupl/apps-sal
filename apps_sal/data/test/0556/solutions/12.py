l, r, k = list(map(int, input().split()))


t = 1
rez = []
for i in range(80):
    if l <= t <= r:
        rez.append(t)
    t *= k
if rez:
    print(*rez)
else:
    print(-1)
