m = list(map(int, input().split()))
w = list(map(int, input().split()))
q = [500, 1000, 1500, 2000, 2500]
s = 0
for i in range(5):
    s += max(0.3 * q[i], (1 - m[i] / 250) * q[i] - 50 * w[i])
h1, h2 = list(map(int, input().split()))
s += 100 * h1
s -= 50 * h2
print(int(s))
