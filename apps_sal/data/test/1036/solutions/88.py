def main():
    text_len, k = [int(x) for x in input().split()]
    text = input()

    text *= 2
    for _ in range(k):
        new_text = ''
        for i in range(0, text_len):
            new_text += janken(text[i * 2], text[i * 2 + 1])
        text = new_text * 2
    return text[0]


def janken(a, b):
    if a == b:
        return a
    if 'P' not in (a, b):
        return 'R'
    if 'S' not in (a, b):
        return 'P'
    if 'R' not in (a, b):
        return 'S'


def __starting_point():
    print((main()))

__starting_point()
