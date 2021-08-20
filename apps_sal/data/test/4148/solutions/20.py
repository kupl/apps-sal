def rot_n():
    n = int(input())
    s = input()
    answer = ''
    for letter in s:
        answer += chr(ord('A') + (ord(letter) - ord('A') + n) % 26)
    print(answer)


def __starting_point():
    rot_n()


__starting_point()
