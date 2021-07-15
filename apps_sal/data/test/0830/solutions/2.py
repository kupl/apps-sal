n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

actions = [ ]
for i in range(k):
    max_index = min_index = 0
    max_value = min_value = a[0]
    for j, value in enumerate(a):
        if value > max_value:
            max_index = j
            max_value = value
        elif value < min_value:
            min_index = j
            min_value = value
    if max_value == min_value:
        break
    actions.append((max_index, min_index))
    a[max_index] -= 1
    a[min_index] += 1
print(max(a) - min(a), len(actions))
for i, j in actions:
    print(i + 1, j + 1)

