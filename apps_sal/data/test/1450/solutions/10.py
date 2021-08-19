t = 1
for test in range(t):
    n = list(input())
    firstZeros = 0
    onesCount = 0
    for i in n:
        if i == '1':
            onesCount += 1
    index = 0
    for i in n:
        if i == '0':
            firstZeros += 1
        elif i == '2':
            break
        index += 1
    print('0' * firstZeros, end='')
    print('1' * onesCount, end='')
    zeroCount = 0
    for i in range(index, len(n)):
        if n[i] == '2':
            print('0' * zeroCount, end='')
            print('2', end='')
            zeroCount = 0
        elif n[i] == '0':
            zeroCount += 1
    print('0' * zeroCount)
