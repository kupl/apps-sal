scales  = input().split('|')
weights = list(input())

balance = len(scales[0]) - len(scales[1])

while weights:
    if len(scales[0]) < len(scales[1]):
        scales[0] += weights[0]
        weights.pop(0)
    else:
        scales[1] += weights[0]
        weights.pop(0)
    balance = len(scales[0]) - len(scales[1])

if balance == 0:
    print('|'.join(scales))
else:
    print('Impossible')



