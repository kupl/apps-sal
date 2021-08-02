our = [input() for i in range(8)]
resA = 100
resB = 100
for i in range(8):
    for j in range(8):
        if our[i][j] == 'W':
            curr = i
            while curr > 0 and our[curr - 1][j] == '.':
                curr -= 1
            if curr == 0:
                resA = min(resA, i)
        elif our[i][j] == 'B':
            curr = i
            while curr < 7 and our[curr + 1][j] == '.':
                curr += 1
            if curr == 7:
                resB = min(resB, curr - i)
if resA <= resB:
    print('A')
else:
    print('B')
