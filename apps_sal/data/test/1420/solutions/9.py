__author__ = 'valeriy.shevchuk'

n, l = map(int, input().split())
data = sorted(list(map(int, input().split())))

max_v = max(data[0], l - data[-1])

for i in range(1, len(data)):
    v = (data[i] - data[i - 1]) / 2
    if v > max_v:
        max_v = v

print(max_v)
