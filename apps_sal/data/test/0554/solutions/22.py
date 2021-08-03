flowers, subarrays = list(map(int, input().split(" ")))
moods = list(map(int, input().split(" ")))
added = 0
for i in range(subarrays):
    f, t = list(map(int, input().split(" ")))
    val = sum(moods[f - 1:t])
    if val > 0:
        added += val
print(added)
