_ = input()
numbers = [int(x) for x in input().split()]
bits = input()

INF = int(1e9)

lowerBoundL = -INF
upperBoundL = INF
lowerBoundR = -INF
upperBoundR = INF

for pos in range(4, len(bits)):
    window = slice(pos - 4, pos + 1)

    if bits[window] == '00000':
        upperBoundL = min(upperBoundL, *numbers[window])
    elif bits[window] == '00001':
        lowerBoundL = max(lowerBoundL, *(x + 1 for x in numbers[window]))
    elif bits[window] == '11111':
        lowerBoundR = max(lowerBoundR, *numbers[window])
    elif bits[window] == '11110':
        upperBoundR = min(upperBoundR, *(x - 1 for x in numbers[window]))

print(lowerBoundL, upperBoundR)
