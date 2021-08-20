string = input().strip()
(letter_first_position, letter_last_position) = ({}, {})
for (position, letter) in enumerate(string):
    if letter not in letter_first_position:
        letter_first_position[letter] = position
    letter_last_position[letter] = position
maximum_distance = max((abs(first_position - last_position) for (first_letter, first_position) in list(letter_first_position.items()) for (last_letter, last_position) in list(letter_last_position.items()) if first_letter != last_letter))
print(maximum_distance)
