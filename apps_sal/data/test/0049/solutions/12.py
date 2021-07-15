n = int(input())
limit_int = limit = decimal = 9
count = 0
while True:
    count += 1
    if n <= limit:
        difference = limit - n
        position = difference % count
        difference = difference // count
        difference = decimal - difference
        print(''.join(list(reversed(str(difference))))[position])
        break
    else:
        decimal = int(str(limit_int) * (count + 1))
        limit += int(str(limit_int) + '0' * count) * (count + 1)

