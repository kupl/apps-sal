n, k = list(map(int, input().split()))
hs = list(map(int, input().split()))
mh = max(hs)
h = []
for i in range(0, mh + 1):
    h.append(0)
for hh in hs:
    h[hh] += 1

l = 0
good = 0
for i in range(mh, 0, -1):
    if h[i] == n:
        break
    if l + h[i] > k:
        good += 1
        l = h[i]
    else:
        l = l + h[i]
    h[i - 1] += h[i]

print(good + (1 if l > 0 else 0))
