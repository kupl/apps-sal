import sys

N = int(sys.stdin.readline())

stations = []
for _ in range(N - 1):
    c, s, f = map(int, sys.stdin.readline().split())
    stations.append((c, s, f))

for i in range(N - 1):
    t = 0
    for j in range(i, N - 1):
        c, s, f = stations[j]
        if t <= s:
            t = s + c
        else:
            tmp = t - s
            t = s + f * ((tmp - 1) // f + 1) + c

    print(t)
print(0)
