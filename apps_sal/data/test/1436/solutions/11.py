n = int(input())
events = list(map(int, input().split()))

police = 0
occur = 0

for i in range(n):
    police += events[i]
    if police < 0:
        occur += 1
        police = 0
print(occur)
