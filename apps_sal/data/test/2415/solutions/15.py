prvky = 'Ac\nAg\nAl\nAm\nAr\nAs\nAt\nAu\nB\nBa\nBe\nBh\nBi\nBk\nBr\nC\nCa\nCd\nCe\nCf\nCl\nCm\nCn\nCo\nCr\nCs\nCu\nDb\nDs\nDy\nEr\nEs\nEu\nF\nFe\nFl\nFm\nFr\nGa\nGd\nGe\nH\nHe\nHf\nHg\nHo\nHs\nI\nIn\nIr\nK\nKr\nLa\nLi\nLr\nLu\nLv\nMd\nMg\nMn\nMo\nMt\nN\nNa\nNb\nNd\nNe\nNi\nNo\nNp\nO\nOs\nP\nPa\nPb\nPd\nPm\nPo\nPr\nPt\nPu\nRa\nRb\nRe\nRf\nRg\nRh\nRn\nRu\nS\nSb\nSc\nSe\nSg\nSi\nSm\nSn\nSr\nTa\nTb\nTc\nTe\nTh\nTi\nTl\nTm\nU\nMc\nLv\nTs\nOg\nV\nW\nXe\nY\nYb\nZn\nZr'.split('\n')
d = {i: [] for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
for i in prvky:
    d[i[0]].append(i)
mem = {}


def f(string):
    if string in mem:
        return mem[string]
    if not string:
        return ''
    for i in d[string[0]]:
        if string.startswith(i.upper()):
            res = f(string[len(i):])
            if res != -1:
                mem[string] = i + res
                return i + res
    return -1


s = input()
r = f(s)
if r == -1:
    print('NO')
else:
    print('YES')
