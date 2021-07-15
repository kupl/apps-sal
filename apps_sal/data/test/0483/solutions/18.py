n = int(input())
velocities = input()
coordinates = input()
speed = [0] * n
time = 10**9

coordinates = list(map(int, coordinates.split()))

for i in range(len(velocities) - 1):
    if velocities[i] == 'R' and velocities[i + 1] == 'L':
        time = min(time, (coordinates[i + 1] - coordinates[i]) // 2)

if time == 10**9:
    time = -1
print(time)
