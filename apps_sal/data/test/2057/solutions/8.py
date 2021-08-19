(n, data) = (int(input()), list(map(int, input().split())))
time = [0] + [-100] * (3 * 10 ** 5)
rooms = [0]
for i in range(1, n + 1):
    if time[data[i - 1]] != -100 and rooms[time[data[i - 1]]] == data[i - 1]:
        rooms[time[data[i - 1]]] = i
        time[i] = time[data[i - 1]]
    else:
        rooms.append(i)
        time[i] = len(rooms) - 1
print(len(rooms))
