Min = 10
total = 0
for i in range(5):
    time = input()
    time = "000" + time
    if time[-1] == "0":
        pass
    else:
        if Min > int(time[-1]):
            Min = int(time[-1])
        time = time[:-1] + "0"
        if time[-2]:
            time = time[-3] + str(int(time[-2]) + 1) + time[-1]
        else:
            time = "10"
    total += int(time)
total -= 10 - Min
print(total)
