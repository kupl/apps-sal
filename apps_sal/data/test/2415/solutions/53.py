strs = 'Ac\nAg\nAl\nAm\nAr\nAs\nAt\nAu\nB\nBa\nBe\nBh\nBi\nBk\nBr\nC\nCa\nCd\nCe\nCf\nCl\nCm\nCn\nCo\nCr\nCs\nCu\nDb\nDs\nDy\nEr\nEs\nEu\nF\nFe\nFl\nFm\nFr\nGa\nGd\nGe\nH\nHe\nHf\nHg\nHo\nHs\nI\nIn\nIr\nK\nKr\nLa\nLi\nLr\nLu\nLv\nMc\nMd\nMg\nMn\nMo\nMt\nN\nNa\nNb\nNd\nNe\nNh\nNi\nNo\nNp\nO\nOg\nOs\nP\nPa\nPb\nPd\nPm\nPo\nPr\nPt\nPu\nRa\nRb\nRe\nRf\nRg\nRh\nRn\nRu\nS\nSb\nSc\nSe\nSg\nSi\nSm\nSn\nSr\nTa\nTb\nTc\nTe\nTh\nTi\nTl\nTm\nTs\nU\nUbb\nUbh\nUbn\nUbp\nUbq\nUbt\nUbu\nUue\nV\nW\nXe\nY\nYb\nZn\nZr'
ele = strs.upper().split('\n')
inp = input()
n = len(inp)
dp = [False] * (n + 1)
dp[0] = True
for i in range(1, n + 1):
    if dp[i - 1] == True and inp[i - 1:i] in ele:
        dp[i] = True
    elif i > 1 and dp[i - 2] == True and (inp[i - 2:i] in ele):
        dp[i] = True
    elif i > 2 and dp[i - 3] == True and (inp[i - 3:i] in ele):
        dp[i] = True
if dp[n]:
    print('YES')
else:
    print('NO')
