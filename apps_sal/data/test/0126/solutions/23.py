n = int(input())
number = input()
numpad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], [None, '0', None]]


def get_coordinates(digit):
    if digit in ('1', '2', '3'):
        first_coordinate = 0
        second_coordinate = int(digit) - 1
    elif digit in ('4', '5', '6'):
        first_coordinate = 1
        second_coordinate = int(digit) - 4
    elif digit in ('7', '8', '9'):
        first_coordinate = 2
        second_coordinate = int(digit) - 7
    else:
        first_coordinate = 3
        second_coordinate = 1
    return (first_coordinate, second_coordinate)


def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])


def sub(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1])


def try_it(start_digit, what_to_do):
    current_coordinates = get_coordinates(start_digit)
    for move in what_to_do:
        current_coordinates = add(current_coordinates, move)
        if current_coordinates[0] < 0 or current_coordinates[1] < 0:
            return False
        try:
            _ = numpad[current_coordinates[0]][current_coordinates[1]]
        except IndexError:
            return False
        if _ is None:
            return False
    return True


sequence = []
for i in range(n - 1):
    sequence.append(sub(get_coordinates(number[i + 1]), get_coordinates(number[i])))
for digit in set('1234567890') - set(number[0]):
    if try_it(digit, sequence):
        print('NO')
        break
else:
    print('YES')
