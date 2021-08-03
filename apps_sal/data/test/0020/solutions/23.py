time = input()
numbers = time.split(":")
hour = int(numbers[0])
minute = int(numbers[1])
total = hour * 60 + minute
minutes = 0
results = "no"
while results != "yes":
    hour = str(int(total / 60) % 24)
    minute = str(total % 60)
    if len(hour) == 1:
        hour = "0" + hour
    if len(minute) == 1:
        minute = "0" + minute
    time = hour + minute
    if time[::-1] == time:
        results = "yes"
        break
    minutes += 1
    total += 1
print(minutes)
