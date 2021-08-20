from math import ceil, log
max_size = -1
for _ in range(int(input().strip())):
    (size, count) = map(int, input().strip().split())
    container = ceil(log(count, 4))
    max_size = max(max_size, size + max(container, 1))
print(max_size)
