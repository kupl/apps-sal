#python3
# utf-8

n = int(input())

list_range = []
list_range += list(range(2, n + 1, 2))
list_range += list(range(1, n + 1, 2))
list_range += reversed(list(range(2, n + 1, 2)))
print(len(list_range))
print(*list_range)

