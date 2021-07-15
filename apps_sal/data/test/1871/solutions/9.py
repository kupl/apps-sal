(n, x) = list(map(int, input().split()))
c = list(map(int, input().split()))
c.sort()
time = 0
for ci in c:
    time += x * ci
    x = max(x - 1, 1)
print(time)

