n = int(input())
pls = [['#','#','#','#'] for i in range(11)]
for i in range(1, 11):
    pls[i][2] = ''
for i in range(11):
    for j in range(4):
        if n == 0:
            break
        if pls[i][j] != '':
            pls[i][j] = 'O'
            n -= 1
print("+------------------------+")
print("|" + pls[0][0], pls[1][0], pls[2][0], pls[3][0], pls[4][0], pls[5][0], pls[6][0], pls[7][0], pls[8][0], pls[9][0], pls[10][0], "|D|)", sep='.')
print("|" + pls[0][1], pls[1][1], pls[2][1], pls[3][1], pls[4][1], pls[5][1], pls[6][1], pls[7][1], pls[8][1], pls[9][1], pls[10][1], "|.|", sep='.')
print("|" + pls[0][2], pls[1][2], pls[2][2], pls[3][2], pls[4][2], pls[5][2], pls[6][2], pls[7][2], pls[8][2], pls[9][2], pls[10][2], "............|", sep='.')
print("|" + pls[0][3], pls[1][3], pls[2][3], pls[3][3], pls[4][3], pls[5][3], pls[6][3], pls[7][3], pls[8][3], pls[9][3], pls[10][3], "|.|)", sep='.')
print("+------------------------+")
