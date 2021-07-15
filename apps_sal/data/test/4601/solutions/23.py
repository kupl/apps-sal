n, k = list(map(int, input().split()))
enemy = list(map(int, input().split()))
enemy = sorted(enemy, reverse=True)
enemy = enemy[k:]
print(sum(enemy))
