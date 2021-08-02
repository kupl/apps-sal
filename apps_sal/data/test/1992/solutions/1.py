n, m, k = map(int, input().split())
apps = list(map(int, input().split()))
runs = list(map(int, input().split()))

places = [0] * (n + 1)
for i in range(n):
    places[apps[i]] = i

touchs = 0
for app in runs:
    place = places[app]
    touchs += place // k + 1
    if place > 0:
        app2 = apps[place - 1]
        apps[place - 1], apps[place] = apps[place], apps[place - 1]
        places[app] = place - 1
        places[app2] = place

print(touchs)
