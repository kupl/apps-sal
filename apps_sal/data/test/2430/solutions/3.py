import sys
f = sys.stdin
#f = open("input.txt", "r")
n = f.readline()
h = [int(i) for i in f.read().strip().split("\n")]
count = h[0] + 1
prev = h[0]
for i in range(1, len(h)):
    if h[i] > prev:
        count += h[i] - prev + 2
        prev = h[i]
    elif h[i] < prev:
        count += prev - h[i] + 2
        prev = h[i]
    elif h[i] == prev:
        count += 2
print(count)
