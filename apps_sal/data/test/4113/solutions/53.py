ans = int(input())
loopFlg = True

for i in range(26):
    if loopFlg == False:
        break
    for j in range(15):
        if 4 * i + 7 * j == ans:
            loopFlg = False


if loopFlg == True:
    print('No')
else:
    print('Yes')
