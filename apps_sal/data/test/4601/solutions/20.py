num, deathblow = map(int, input().split())
enemy_table = list(map(int, input().split()))
list.sort(enemy_table, reverse=True)
sum = 0
if num <= deathblow:
    print(0)
else:
    for i in range(deathblow):
        enemy_table[i] = 0
    for j in range(num):
        sum += enemy_table[j]
    print(sum)
