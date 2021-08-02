import sys

n = int(sys.stdin.readline())
tracker = {}
count = 0

for i in range(n):
    pair = sys.stdin.readline().split("\n")[0].split(" ")
    if (pair[0] in tracker):
        tracker[pair[1]] = tracker.pop(pair[0])
    else:
        count += 1
        tracker[pair[1]] = pair[0]

print(count)
for key in list(tracker.keys()):
    print(tracker[key] + " " + key)
