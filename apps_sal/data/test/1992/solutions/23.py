#!/bin/python

apps_size, launched_size, apps_per_screen = list(map(int, input().split()))

apps = list(map(int, input().split()))
launched = list(map(int, input().split()))

apps_pos = {}
for pos, elem in enumerate(apps):
    apps_pos[elem] = pos

result = 0
for app in launched:
    pos = apps_pos[app]
    if pos == 0:
        result += 1
        continue
    prev_app = apps[pos-1]

    result += pos // apps_per_screen + 1

    apps[pos-1] = app
    apps[pos] = prev_app
    apps_pos[prev_app] = pos
    apps_pos[app] = pos-1

print(result)

