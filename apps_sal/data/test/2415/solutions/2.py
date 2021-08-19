l = 'H\nHe\nLi\nBe\nB\nC\nN\nO\nF\nNe\nNa\nMg\nAl\nSi\nP\nS\nCl\nAr\nK\nCa\nSc\nTi\nV\nCr\nMn\nFe\nCo\nNi\nCu\nZn\nGa\nGe\nAs\nSe\nBr\nKr\nRb\nSr\nY\nZr\nNb\nMo\nTc\nRu\nRh\nPd\nAg\nCd\nIn\nSn\nSb\nTe\nI\nXe\nCs\nBa\nLa\nCe\nPr\nNd\nPm\nSm\nEu\nGd\nTb\nDy\nHo\nEr\nTm\nYb\nLu\nHf\nTa\nW\nRe\nOs\nIr\nPt\nAu\nHg\nTl\nPb\nBi\nPo\nAt\nRn\nFr\nRa\nAc\nTh\nPa\nU\nNp\nPu\nAm\nCm\nBk\nCf\nEs\nFm\nMd\nNo\nLr\nRf\nDb\nSg\nBh\nHs\nMt\nDs\nRg\nCn\nNh\nFl\nMc\nLv\nTs\nOg'.split()
l = list([x.lower() for x in l])
inp = input().strip().lower()
dp = [True]
for i in range(len(inp)):
    works = False
    if dp[-1] and inp[i] in l:
        works = True
    if i and dp[-2] and (inp[i - 1:i + 1] in l):
        works = True
    dp.append(works)
if dp[-1]:
    print('YES')
else:
    print('NO')
