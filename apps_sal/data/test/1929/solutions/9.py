(n, t, c) = list(map(int, input().split()))
ps = list(map(int, input().split()))
bs = []
bs.append(0)
for i in range(n):
    if ps[i] > t:
        bs.append(i + 1)
bs.append(n + 1)
print(sum((bs[i] - bs[i - 1] - c for i in range(1, len(bs)) if bs[i] - bs[i - 1] > c)))
