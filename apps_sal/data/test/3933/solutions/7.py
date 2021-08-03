input()
a = list(map(int, input().split()))
diffs = [a[n] - a[n - 1] for n in range(1, len(a))]

print((a[-1] + diffs[0]) if len(set(diffs)) == 1 else a[-1])
