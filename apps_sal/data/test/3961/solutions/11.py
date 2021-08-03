no_rooms = int(input())
links = [None] + [int(x) for x in input().split()]
paths = [0] * (no_rooms + 2)  # last is total

for i in range(1, no_rooms + 1):
    paths[i + 1] = (2 * paths[i] - paths[links[i]] + 2) % 1000000007

print(paths[no_rooms + 1] % 1000000007)
