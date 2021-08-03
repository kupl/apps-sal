A, B = map(int, input().split())
socket = 1
taps = 0
while True:
    if socket >= B:
        break
    else:
        taps += 1
        socket = socket + (A - 1)
print(taps)
