n = int(input())
a = [int(x) for x in input().split()]
alive = 0
minKillIndex = n
for i in range(n - 1, -1, -1):
    if i < minKillIndex:
        alive += 1
    minKillIndex = min(i - a[i], minKillIndex)

print(alive)
