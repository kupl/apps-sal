n = int(input())
a = list(map(int, input(). split()))
sl = []
s2 = []
for i in range(n - 2):
    sl += [a[i + 2] - a[i]]
    s2 += [a[i + 1] - a[i]]
s2 += [a[-1] - a[-2]]
print(max(min(sl), max(s2)))
