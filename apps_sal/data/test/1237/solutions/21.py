class Event:
    def __init__(self, floor, time):
        self.floor, self.time = floor, time


n, floor = list(map(int, input().split()))
events = [Event(*list(map(int, input().split()))) for i in range(n)]
events.sort(key=lambda event: (-event.floor, event.time))

time = 0
for event in events:
    time = max(event.time, time + floor - event.floor)
    floor = event.floor
time += floor
print(time)
