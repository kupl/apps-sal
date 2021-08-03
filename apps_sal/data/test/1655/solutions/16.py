n = int(input())
kog = list(map(int, input().split()))

alive = 1
kill = kog[n - 1]
for i in range(n - 2, -1, -1):
    if kill == 0:
        alive = alive + 1
    kill = max(kill - 1, kog[i])

print(alive)
