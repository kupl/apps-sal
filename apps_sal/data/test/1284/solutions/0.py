x = int(input())
y = list(map(int, input().split(' ')))
bad = x // 2
s = 0
t = 0
y = y + y
for i in range(bad):
    s += y[2 * i]
    t += y[2 * i + 1]
mini = min(s, t)
for i in range(bad):
    s -= y[2 * i]
    s += y[2 * (bad + i)]
    t -= y[2 * i + 1]
    t += y[2 * (bad + i) + 1]
    mini = min(mini, min(s, t))
print(sum(y) // 2 - mini)
