m = list(map(int, input().split()))
w = list(map(int, input().split()))
hs, hu = map(int, input().split())

s = [500 * (x + 1) for x in range(5)]

for i in range(5):
    s[i] = max(0.3 * s[i], (1 - m[i] / 250) * s[i] - 50 * w[i])

s_t = sum(s) + 100 * hs - 50 * hu

print(int(s_t))
