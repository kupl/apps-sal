"""
Read tutorial, graph the moves, still don't understand this problem
"""


def nineteen(string_str) -> int:
    letter_count_dict = dict()
    for letter in string_str:
        if letter_count_dict.get(letter, 0) == 0:
            letter_count_dict[letter] = 1
        else:
            letter_count_dict[letter] += 1
    nineteen_count = 0
    while letter_count_dict.get('n', 0) >= 3 and letter_count_dict.get('i', 0) >= 1 and (letter_count_dict.get('e', 0) >= 3) and (letter_count_dict.get('t', 0) >= 1):
        letter_count_dict['n'] -= 2
        letter_count_dict['i'] -= 1
        letter_count_dict['e'] -= 3
        letter_count_dict['t'] -= 1
        nineteen_count += 1
    return nineteen_count


def __starting_point():
    """
    Inside of this is the test. 
    Outside is the API
    """
    string = input()
    print(nineteen(string))


__starting_point()
