n = int(input())
an = list(map(int, input().split()))
zyunban = [0] * n
t = 1
for x in an:
    zyunban[x - 1] = t
    t += 1
zyunban = list(map(str, zyunban))
print(' '.join(zyunban))
