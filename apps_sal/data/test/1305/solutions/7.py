n = input()
queue = input().split()
p25 = 0
p50 = 0
p100 = 0
result = 'YES'
for note in queue:
    if note == '25':
        p25 += 1
    elif note == '50':
        if p25 > 0:
            p50 += 1
            p25 -= 1
        else:
            result = 'NO'
            break
    elif note == '100':
        if p50 > 0 and p25 > 0:
            p50 -= 1
            p25 -= 1
            p100 += 1
        elif p25 > 2:
            p25 -= 3
            p100 += 1
        else:
            result = 'NO'
            break
print(result)
