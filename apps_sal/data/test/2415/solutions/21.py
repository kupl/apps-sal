elems = 'Ac\nAl\nAm\nSb\nAr\nAs\nAt\nBa\nBk\nBe\nBi\nBh\nB\nBr\nCd\nCa\nCf\nC\nCe\nCs\nCl\nCr\nCo\nCu\nCm\nDs\nDb\nDy\nEs\nEr\nEu\nFm\nF\nFr\nGd\nGa\nGe\nAu\nHf\nHs\nHe\nHo\nH\nIn\nI\nIr\nFe\nKr\nLa\nLr\nPb\nLi\nLu\nMg\nMn\nMt\nMd\nHg\nMo\nNd\nNe\nNp\nNi\nNb\nN\nNo\nUuo\nOs\nO\nPd\nP\nPt\nPu\nPo\nK\nPr\nPm\nPa\nRa\nRn\nRe\nRh\nRg\nRb\nRu\nRf\nSm\nSc\nSg\nSe\nSi\nAg\nNa\nSr\nS\nTa\nTc\nTe\nTb\nTl\nTh\nTm\nSn\nTi\nW\nU\nV\nXe\nYb\nY\nZn\nZr\nCn\nNh\nFl\nMc\nLv\nTs\nOg'.upper().split('\n')


def does_it_work(word):
    if word == '':
        return True
    for x in elems:
        if word.startswith(x) and does_it_work(word[len(x):]):
            return True
    return False


print('YES' if does_it_work(input()) else 'NO')
