n = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))

cumsum_t = [0] * (n + 1)
for i in range(n):
    cumsum_t[i + 1] = cumsum_t[i] + t[i]

v_max = [0] * (2 * sum(t) + 1)
for i in range(len(cumsum_t) - 1):
    for j in range(2 * cumsum_t[i], 2 * cumsum_t[i + 1]):
        v_max[j] = v[i]
for i in range(len(cumsum_t) - 1):
    v_max[cumsum_t[i + 1] * 2] = min(v_max[cumsum_t[i + 1] * 2], v[i])

speed = [101] * (2 * sum(t) + 1)
speed[0] = 0
speed[-1] = 0
for i in range(len(speed) - 1):
    speed[i + 1] = min(speed[i + 1], speed[i] + 0.5, v_max[i + 1])
for i in range(len(speed) - 1)[::-1]:
    speed[i] = min(speed[i], speed[i + 1] + 0.5, v_max[i])

print(sum(speed) / 2)
