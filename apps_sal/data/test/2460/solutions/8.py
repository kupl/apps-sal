import sys

num_riders, _ = list(map(int, next(sys.stdin).split()))

houses = list(map(int, next(sys.stdin).split()))
is_rider = list(map(int, next(sys.stdin).split()))

current_left_driver = None
current_citizens = []

result = []

for house, is_rider in zip(houses, is_rider):
    if is_rider:
        if current_left_driver is None:
            result.append(len(current_citizens))
        else:
            result.append(0)
            for citizen in current_citizens:
                if abs(citizen - current_left_driver) <= abs(citizen - house):
                    result[-2] += 1
                else:
                    result[-1] += 1

        current_citizens = []
        current_left_driver = house
    else:
        current_citizens.append(house)

result[-1] += len(current_citizens)

print(' '.join(map(str, result)))

