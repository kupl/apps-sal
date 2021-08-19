n = int(input())
times = []
for _ in range(n):
    time = str(input())
    times.append((int(time[:2]), int(time[3:])))
times.sort()


def to_minutes(a):
    return 60 * a[0] + a[1]


def to_hours(a):
    return (a // 60, a % 60)


def pad(a):
    return ('0' if a < 10 else '') + str(a)


longest = 0
for i in range(1, n):
    longest = max(longest, to_minutes(times[i]) - to_minutes(times[i - 1]))
longest = max(longest, 60 * 24 + to_minutes(times[0]) - to_minutes(times[n - 1]))
longest -= 1
(hours, minutes) = to_hours(longest)
print(pad(hours), ':', pad(minutes), sep='')
