m = list(map(int, input().split(' ')))
w = list(map(int, input().split(' ')))
(hs, hu) = list(map(int, input().split(' ')))
s = 0
s += hs * 100 - hu * 50
for i in range(5):
    s += max(0.3 * ((i + 1) * 500), (1 - m[i] / 250) * ((i + 1) * 500) - 50 * w[i])
print(int(s))
