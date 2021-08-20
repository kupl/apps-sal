k = '\t\nH\t\nHe\t\nLi\nBe\t\nB\nC\nN\nO\nF\nNe\t\nNa\nMg\t\nAl\nSi\nP\nS\nCl\nAr\t\nK\nCa\t\nSc\nTi\nV\nCr\nMn\nFe\nCo\nNi\nCu\nZn\nGa\nGe\nAs\nSe\nBr\nKr\n5\t\nRb\nSr\t\nY\nZr\nNb\nMo\nTc\nRu\nRh\nPd\nAg\nCd\nIn\nSn\nSb\nTe\nI\nXe\t\nCs\nBa\nLa\nCe\nPr\nNd\nPm\nSm\nEu\nGd\nTb\nDy\nHo\nEr\nTm\nYb\nLu\nHf\nTa\nW\nRe\nOs\nIr\nPt\nAu\nHg\nTl\nPb\nBi\nPo\nAt\nRn\t\nFr\nRa\nAc\nTh\nPa\nU\nNp\nPu\nAm\nCm\nBk\nCf\nEs\nFm\nMd\nNo\nLr\nRf\nDb\nSg\nBh\nHs\nMt\nDs\nRg\nCn\nNh\nFl\nMc\nLv\nTs\nOg\t\nUue\nUbn\nUbu\nUbb\nUbt\nUbq\nUbp\nUbh\nUbs\n'.upper().split()
s = '0' + input()
dp = [0] * len(s)
dp[0] = 1
for i in range(1, len(s)):
    for j in range(1, 3):
        if s[i - j + 1:i + 1] in k:
            dp[i] |= dp[i - j]
print('YES' if dp[-1] else 'NO')
