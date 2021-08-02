n = int(input())
d = []
for _ in range(n):
    l, r = [int(item) for item in input().split()]
    d.append([l, r])

k = int(input())

ans = 0
for i in range(n):
    l, r = d[i]
    if r >= k:
        ans = i
        break

print(n - ans)
