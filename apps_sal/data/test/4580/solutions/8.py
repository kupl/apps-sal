n = int(input())
rate = list(map(int, input().split()))
v = [0] * 9
for i in range(n):
    c = int(rate[i] / 400)
    if c >= 8:
        v[8] += 1
    else:
        v[c] = 1
s = sum(v[:8])
mi = max(1, s)
ma = s + v[8]
print(mi, ma)
