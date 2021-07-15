from sys import stdin,stderr
def rl():
    return [int(w) for w in stdin.readline().split()]

n, end_day = rl()
d = rl()

start_month = start_day = end_month = hugs = 0
while end_month < n and end_day >= d[end_month]:
    hugs += (d[end_month] * (d[end_month] + 1)) // 2
    end_day -= d[end_month]
    end_month += 1
hugs += (end_day * (end_day + 1)) // 2

max_hugs = hugs
if end_month < n:
    while start_month < n:
        step = min(d[start_month] - start_day, d[end_month] - end_day)
        hugs += step * (end_day - start_day)
        start_day += step
        if start_day >= d[start_month]:
            start_day = 0
            start_month += 1
        end_day += step
        if end_day >= d[end_month]:
            end_day = 0
            end_month += 1
            if end_month >= n:
                end_month = 0
        if hugs > max_hugs:
            max_hugs = hugs

print(max_hugs)

