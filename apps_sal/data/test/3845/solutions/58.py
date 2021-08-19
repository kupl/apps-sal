(A, B) = list(map(int, input().split()))
white = [['.'] * 100 for _ in range(50)]
black = [['#'] * 100 for _ in range(50)]
flag = True
if B != 1:
    for h in range(0, 50, 2):
        if flag:
            for w in range(0, 100, 2):
                white[h][w] = '#'
                B -= 1
                if B == 1:
                    flag = False
                if flag == False:
                    break
        if flag == False:
            break
flag = True
if A != 1:
    for h in range(1, 50, 2):
        if flag:
            for w in range(0, 100, 2):
                black[h][w] = '.'
                A -= 1
                if A == 1:
                    flag = False
                if flag == False:
                    break
        if flag == False:
            break
print((100, 100))
for w in white:
    print(''.join(w))
for b in black:
    print(''.join(b))
