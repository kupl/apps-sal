import sys

n = int(sys.stdin.readline())
start = dict()
end = dict()
for i in range(n):
    b, c = (int(s) for s in sys.stdin.readline().rstrip().split(' '))
    start[b] = start.setdefault(b, 0) + 1
    start.setdefault(c, 0)
    end[c] = end.setdefault(c, 0) + 1
    end.setdefault(b, 0)
keys = sorted(start.keys())
k = 0
a = [0 for x in range(n+1)]
prev = -1
start_c = 0
end_c = 0
for key in keys:
    if prev != -1 and key - prev > 1:
        a[start_c - end_c] += key - prev - 1
    start_c += start[key]
    a[start_c - end_c] += 1
    end_c += end[key]
    prev = key
print(' '.join(str(x) for x in a[1:n+1]))
