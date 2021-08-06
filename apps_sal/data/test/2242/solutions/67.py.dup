N = str(input())
n, mods = 0, [1] + [0] * 2018
d = 1
for i in reversed(N):
    n = (n + int(i) * d) % 2019
    mods[n] += 1
    d = (d * 10) % 2019

print(sum([i * (i - 1) // 2 for i in mods]))
