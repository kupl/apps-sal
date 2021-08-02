n = int(input())
top = [0]
bot = [0]
top += [int(i) for i in input().split()]
bot += [int(i) for i in input().split()]
cross = [int(i) for i in input().split()]

for i in range(1, n):
    top[i] += top[i - 1]
    bot[i] += bot[i - 1]

best = 11111111111111;
best2 = 11111111111111;

for i in range(n):
    dist = top[i] + cross[i] + (bot[n - 1] - bot[i])
    if dist < best2:
        if dist <= best:
            best2 = best
            best = dist
        else:
            best2 = dist

print(best + best2)
