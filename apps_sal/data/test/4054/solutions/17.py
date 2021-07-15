requirements = (1, 1, 2, 7, 4)

ingrs = [int(x) for x in input().split(" ")]

min_count = 2**64

for i, x in enumerate(ingrs):
    if i >= len(requirements):
        continue
    min_count = min(int(x / requirements[i]), min_count)

print(min_count)

