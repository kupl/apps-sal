s = int(input(), 2)

count = 0
i = 0
while True:
    if 4**i >= s:
        break
    count += 1
    i += 1
print(count)

