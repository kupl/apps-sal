#!/usr/bin/env python
a, t_a = list(map(int, input().split()))
b, t_b = list(map(int, input().split()))
hh, mm = list(map(int, input().split(sep=':')))
start_time = (hh - 5) * 60 + mm
buses = []
for time in range((24 - 5) * 60):
    if time < start_time:
        buses = [item - 1 for item in buses if item != 1]
        if time % b == 0:
            buses.append(t_b)
    elif time == start_time:
        buses = [item - 1 for item in buses if item != 1]
        z = len(buses)
    if time >= start_time and time < start_time + t_a:
        if time % b == 0:
            z += 1
print(z)
