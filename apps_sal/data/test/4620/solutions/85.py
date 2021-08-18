n = int(input())
cl = []
sl = []
fl = []

for _ in range(n - 1):
    c, s, f = list(map(int, input().split()))
    cl += [c]
    sl += [s]
    fl += [f]


for i in range(n):
    time = 0
    while True:
        if i == n - 1:
            print(time)
            break
        if sl[i] <= time and time % fl[i] == 0:
            time += cl[i]
        elif sl[i] > time:
            time = sl[i] + cl[i]
        else:
            time += fl[i] - time % fl[i] + cl[i]
        i += 1
