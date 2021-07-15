n = int(input())
times = [0] * 2880
for _ in range(n):
    hh, mm = map(int, input().split(':'))
    t = hh * 60 + mm
    times[t] = 1
    times[t + 1440] = 1

i = 0
res = -1
while i < 1440:
    for j in range(i, i + 1440):
        if times[j] == 1:
            break
    res = max(res, j - i)
    i = j + 1
hh, mm = divmod(res, 60)
print('{:02d}:{:02d}'.format(hh, mm))
