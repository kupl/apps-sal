import sys
input = sys.stdin.readline
T = int(input())

for t in range(T):
    s = input()[:-1]

    counts = []
    current = 0
    for c in s:
        if c == '1':
            current += 1
        else:
            counts.append(current)
            current = 0
    if current:
        counts.append(current)

    res = 0
    counts = sorted(counts, reverse=True)
    for i in range(len(counts)):
        if 2 * i >= len(counts):
            break
        res += counts[2 * i]
    print(res)
