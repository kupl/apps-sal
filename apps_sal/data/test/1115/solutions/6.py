n = int(input())
t = sum(map(int, input().split()))
m = int(input())
possible = False
best = 1000000000
for i in range(m):
    l,r = list(map(int, input().split()))
    if l <= t <= r:
        possible = True
    if l >= t:
        best = min(best, l)
if possible:
    print(t)
elif best < 1000000000:
    print(best)
else:
    print(-1)

