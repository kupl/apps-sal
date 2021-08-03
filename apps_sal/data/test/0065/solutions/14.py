
n = input()
arr = list(map(int, input().strip().split()))

mini = None
min_dist = None
positions = []
last = -1
for i, a in enumerate(arr):
    if mini is None or a < mini:
        mini = a
        last = i
        min_dist = None
    elif mini == a:
        d = i - last
        if min_dist is None or d < min_dist:
            min_dist = d
        last = i
print(min_dist)
