n = int(input())

data = input()

available_keys = {}
needed_keys = 0

k = 0
for _ in range(n - 1):
    key = data[k]
    lock = data[k + 1].lower()

    k += 2

    available_keys[key] = available_keys.get(key, 0) + 1

    if available_keys.get(lock, 0):
        available_keys[lock] -= 1
    else:
        needed_keys += 1

print(needed_keys)
