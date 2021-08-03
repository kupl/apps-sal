import sys


input = []
input_index = 0


def next(type, number=None):
    def next():
        nonlocal input, input_index

        while input_index == len(input):
            if sys.stdin:
                input = sys.stdin.readline().split()
                input_index = 0
            else:
                raise Exception()

        input_index += 1

        return input[input_index - 1]

    if number is None:
        result = type(next())
    else:
        result = [type(next()) for _ in range(number)]

    return result


s = next(str)

_abs = []
_bas = []

for index in range(1, len(s)):
    if s[index - 1:index + 1] == "AB":
        _abs.append(index)
    elif s[index - 1:index + 1] == "BA":
        _bas.append(index)

if _abs and _bas and abs(min(_abs) - max(_bas)) >= 2:
    print("YES")
elif _abs and _bas and abs(max(_abs) - min(_bas)) >= 2:
    print("YES")
else:
    print("NO")
