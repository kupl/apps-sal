n, m = list(map(int, input().split()))
d = dict([input().split() for _ in range(m)])
print(" ".join([min((w, d[w]), key=len) for w in input().strip().split()]))

