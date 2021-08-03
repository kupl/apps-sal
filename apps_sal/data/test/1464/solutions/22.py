from itertools import product


def generate_name(S):
    for i in range(1, 9):
        for letters in product('abcdefghijklmnopqrstuvwxyz', repeat=i):
            name = ''.join(letters)
            if all(name not in s for s in S):
                return name


print(generate_name([input() for _ in range(int(input()))]))
