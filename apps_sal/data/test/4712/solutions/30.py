H, W = [int(x) for x in input().split()]

for i in range(H):
    if i == 0:
        print((''.join(['#'] * (W + 2))))

    print(('#' + input() + '#'))

print((''.join(['#'] * (W + 2))))
