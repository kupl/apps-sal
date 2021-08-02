
def get_solution(source, desired_len, alphabet):
    if desired_len <= len(source):
        target = source[:desired_len]
        last_non_terminal = get_last_non_terminal(target, alphabet)
        target = target[:last_non_terminal] + next_char(target[last_non_terminal], alphabet)
    else:
        target = source

    return pad_with_starters(target, desired_len, alphabet)


def get_last_non_terminal(target, alphabet):
    for i, char in reversed(list(enumerate(target))):
        if char != alphabet[-1]:
            return i


def next_char(char, alphabet):
    return alphabet[alphabet.index(char) + 1]


def pad_with_starters(target, desired_len, alphabet):
    return target + (desired_len - len(target)) * alphabet[0]


_, desired_len = [int(x) for x in input().split()]
source = input()
alphabet = list(set(source))
alphabet.sort()

print(get_solution(source, desired_len, alphabet))
