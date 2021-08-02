n, m = map(int, input().split())

food = [0] * (m + 1)
for i in range(n):
    l = [int(x) for x in input().split()]
    l = set(l[1:])
    for x in l:
        food[x] += 1

ans = food.count(n)
print(ans)
