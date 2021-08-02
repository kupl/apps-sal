x, n = map(int, input().split())
p = sorted([int(x) for x in input().split()])

if n == 0:
    print(x)
    return

ans = idx = 10**9
for i in range(-500, 500):
    for pi in p:
        if p.count(i) == 0:
            if ans > abs(i - x):
                ans = abs(i - x)
                idx = i
print(idx)
