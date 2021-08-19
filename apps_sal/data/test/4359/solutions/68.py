from math import ceil
time = [int(input()) for i in range(5)]
mod = [i % 10 for i in time]
a = 124
res = 0
for i in range(len(mod)):
    if mod[i] != 0:
        a = min(a, mod[i])
if a == 124:
    a = 0
for i in range(5):
    if i == mod.index(a):
        res += time[i]
    else:
        res += ceil(time[i] / 10) * 10
print(res)
