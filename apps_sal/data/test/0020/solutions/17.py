time = input()
b = time.find(':')
h = int(time[:b])
m = int(time[b + 1:])
for i in range(60 * 24):
    time = "0" * (2 - len(str(h))) + str(h) + "0" * (2 - len(str(m))) + str(m)
    if time == time[::-1]:
        print(i)
        return
    m += 1
    h += m // 60
    h %= 24
    m %= 60

