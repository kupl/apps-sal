n = int(input())

people = list(map(int, input().split()))

count = 0

for i in range(n):
    if i == 0 or people[i - 1] <= people[i]:
        continue
    else:
        count += people[i - 1] - people[i]
        people[i] += people[i - 1] - people[i]
print(count)
