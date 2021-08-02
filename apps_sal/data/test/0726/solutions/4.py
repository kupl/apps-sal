n, d = [int(x) for x in input().strip().split()]
x = [int(x) for x in input().strip().split()]

d *= 2
x.sort()

ans = 2
for i in range(len(x) - 1):
    diff = x[i + 1] - x[i]
    if diff == d:
        ans += 1
    elif diff > d:
        ans += 2

print(ans)
