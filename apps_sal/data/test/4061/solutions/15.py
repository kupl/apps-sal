from sys import stdin
input = stdin.readline

s = input()
t = input()

n = len(t)
low = [0 for i in range(len(t))]
high = [0 for i in range(len(t))]

acc = 0

for i in range(n):
    acc_t = t[i]

    while acc_t != s[acc]: acc += 1
    low[i] = acc
    acc += 1

acc = len(s) - 1

for i in range(len(t)):
    acc_t = t[n - i - 1]

    while acc_t != s[acc]: acc -= 1
    high[n - i - 1] = acc
    acc -= 1

res = max(high[0], len(s) - low[n - 1] - 1)

for i in range(n - 1):
    res = max(res, high[i + 1] - low[i] - 1)

print(res)
