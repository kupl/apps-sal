input()
round_counter = 0
counter = 0
for x in [int(y) for y in input().split(' ') if y in '12345']:
    if x > 3:
        round_counter += 1
        if round_counter == 3:
            counter += 1
            round_counter = 0
    if round_counter < 3 and x <= 3:
        round_counter = 0
print(counter)
