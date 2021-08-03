n = int(input())
p = [int(i) for i in input().split()]

kills = 0
claw = p[-1]
for i in range(n - 2, -1, -1):
    if claw > 0:
        kills += 1
    claw -= 1
    if p[i] > claw:
        claw = p[i]

print(n - kills)
