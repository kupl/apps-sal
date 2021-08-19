n = int(input())
timetable = [list(map(int, input().split())) for _ in range(n - 1)]


def nextstn(t, stn):
    if t >= timetable[stn][1]:
        return (t + timetable[stn][2] - 1) // timetable[stn][2] * timetable[stn][2] + timetable[stn][0]
    else:
        return timetable[stn][1] + timetable[stn][0]


for i in range(n - 1):
    current_stn = i
    laps = 0
    while current_stn < n - 1:
        laps = nextstn(laps, current_stn)
        current_stn += 1
    print(laps)
else:
    print(0)
