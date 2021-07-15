a = list(input().split())
n, T, c = int(a[0]), int(a[1]), float(a[2])
a = list(map(int, input().split()))
m = int(input())
p = list(map(int, input().split()))

sum_a = sum(a[:T - 1])
mean = 0
for t in range(T - 1):
    mean = (mean + a[t]/T) / c

i = 0
for t in range(T - 1, p[-1]):
    sum_a += a[t]
    mean = (mean + a[t]/T) / c
    if t == p[i] - 1:
        real = sum_a / T
        print('%0.6f %0.6f %0.6f' % (real, mean, abs(real - mean) / real))
        i += 1
        if i == len(p) : break
    sum_a -= a[t - T + 1]

