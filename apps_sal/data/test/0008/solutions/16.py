s = input().split()
hand = {'m': [], 'p': [], 's': []}
for item in s:
    hand[item[1]].append(int(item[0]))
min_steps_needed = 10
for symb in ['m', 'p', 's']:
    hand[symb] = sorted(hand[symb])
    for start in range(1, 10):
        a_needed = 10
        b_needed = 10
        a_needed = 3 - hand[symb].count(start)
        (b1, b2, b3) = (0, 0, 0)
        if hand[symb].count(start) > 0:
            b1 = 1
        if hand[symb].count(start + 1) > 0:
            b2 = 1
        if hand[symb].count(start + 2) > 0:
            b3 = 1
        b_needed = 3 - b1 - b2 - b3
        if a_needed < min_steps_needed:
            min_steps_needed = a_needed
        if b_needed < min_steps_needed:
            min_steps_needed = b_needed
print(min_steps_needed)
