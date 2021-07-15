def score(m, w, x):
    return max(0.3*x, (1.0 - m/250) * x - 50*w)

ms = list(map(int, input().split()))
ws = list(map(int, input().split()))
hs, hu = list(map(int, input().split()))

score = sum(score(m, w, x) for m, w, x in zip(ms, ws, [500,1000,1500,2000,2500]))
print(int(score + 100 * hs - 50 * hu))

