(n, x) = list(map(int, input().split()))
c = list(map(int, input().split()))
d = [0] * 100001
for ci in c:
    d[ci] += 1
time = 0
ci = 1
while ci < 100001:
    if d[ci] > 0:
        time += x * ci
        d[ci] -= 1
        x = max(1, x - 1)
    else:
        ci += 1
print(time)
