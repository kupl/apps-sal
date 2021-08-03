start = input().split(":")
end = input().split(":")

start[0], start[1], start[2] = int(start[0]), int(start[1]), int(start[2])

end[0], end[1], end[2] = int(end[0]), int(end[1]), int(end[2])


if((start[0] > end[0]) or (start[0] == end[0] and start[1] > end[1]) or (start[0] == end[0] and start[1] == end[1] and start[2] > end[2])):
    e = list(start)
    s = list(end)
else:
    e = list(end)
    s = list(start)
days = 0
for i in range(s[0] + 1, e[0]):
    if(i % 400 == 0):
        days += 366
    elif(i % 100 == 0):
        days += 365
    elif(i % 4 == 0):
        days += 366
    else:
        days += 365

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if(s[0] % 400 == 0):
    month[1] += 1
elif(s[0] % 100 == 0):
    month[1] = 28
elif(s[0] % 4 == 0):
    month[1] += 1

for i in range(s[1] + 1, 13):
    days += month[i - 1]

month[1] = 28

if(e[0] % 400 == 0):
    month[1] += 1
elif(e[0] % 100 == 0):
    month[1] = 28
elif(e[0] % 4 == 0):
    month[1] += 1

for i in range(0, e[1] - 1):
    days += month[i]
month[1] = 28
if(s[0] % 400 == 0):
    month[1] += 1
elif(s[0] % 100 == 0):
    month[1] = 28
elif(s[0] % 4 == 0):
    month[1] += 1
days += e[2]
days += month[s[1] - 1] - s[2]

if(s[0] == e[0]):
    days = 0
    for i in range(s[1] + 1, e[1]):
        days += month[i - 1]
    days += e[2]
    days += month[s[1] - 1] - s[2]
if(s[0] == e[0] and s[2] == e[2]):

    days = 0
    for i in range(s[1], e[1]):
        days += month[i - 1]
if(s[0] == e[0] and s[1] == e[1]):
    days = e[2] - s[2]
if(s[0] == e[0] and s[1] == e[1] and s[2] == e[2]):
    days = 0

print(days)
