n = int(input())
inp = input().split(' ')
people = []
for i in range(n):
    people.append(int(inp[i]))
inp = input().split(' ')
start = int(inp[0])
end = int(inp[1])
diff = end - start
optimal = 1
people = people + people
m = sum(people[0:diff])
prev_sum = m
for i in range(1, n):
    offset = min(diff, n - i)
    prev_sum -= people[i - 1]
    prev_sum += people[i + diff - 1]
    if prev_sum > m:
        m = prev_sum
        optimal = i + diff
        optimal = (end - optimal) % n
        if optimal == 0:
            optimal = n
    if prev_sum == m:
        optimal2 = i + diff
        optimal2 = (end - optimal2) % n
        if optimal2 == 0:
            optimal2 = n
        if optimal2 < optimal:
            optimal = optimal2
if m == 0:
    optimal = 1
print(optimal)
