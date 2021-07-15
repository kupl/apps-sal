import sys

ghosts, duration, candles = input().split()
arrival = input().split()
burn = []
for j in range(len(arrival)):
    time = int(arrival[len(arrival) - 1 - j])
    candle = int(candles)
    if len(burn) != 0:
        for k in range(len(burn)):
            if burn[k] <= time:
                candle -= 1
    for i in range(candle):
        burn.append(time - int(duration) + 1 + i)
    if burn[-1] > time:
        print('-1')
        return
print(len(burn))

