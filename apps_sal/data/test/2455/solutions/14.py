#!/usr/local/bin/python33
n = int(input())

for i in range(n):
    cnt = 0
    answ = ['1x12', '2x6', '3x4', '4x3', '6x2', '12x1']
    answb = [False, False, False, False, False, False]
    instr = input()

    if 'X' in instr:
        cnt += 1
        answb[0] = True
    for j in range(6):
        if (instr[j] == instr[6 + j] == 'X'):
            cnt += 1
            answb[1] = True
            break
    for j in range(4):
        if (instr[j] == instr[4 + j] == instr[8 + j] == 'X'):
            cnt += 1
            answb[2] = True
            break
    for j in range(3):
        if (instr[j] == instr[3 + j] == instr[6 + j] == instr[9 + j] == 'X'):
            cnt += 1
            answb[3] = True
            break
    for j in range(2):
        if (instr[j] == instr[2 + j] == instr[4 + j] == instr[6 + j] == instr[8 + j] == instr[10 + j] == 'X'):
            cnt += 1
            answb[4] = True
            break
    if not 'O' in instr:
        cnt += 1
        answb[5] = True

    print(cnt, end=' ')
    for i in range(6):
        if answb[i]:
            print(answ[i], end=' ')
    print()
