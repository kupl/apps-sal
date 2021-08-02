import sys
input = sys.stdin.read()
direction, string = input.split()

keyboard = ['qwertyuiop', 'asdfghjkl;', 'zxcvbnm,./']


def modify(char):
    shift = +1 if direction == "L" else -1
    for row in keyboard:
        if char in row:
            return row[row.find(char) + shift]
    else:
        print("Error:", char, shift)
        assert False


sys.stdout.write("".join(map(modify, string)))
