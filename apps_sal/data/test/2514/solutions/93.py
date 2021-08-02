N = int(input())
List = list(map(int, input().split()))
Row = int(input())
QList = []
for i in range(Row):
    QList.append(list(map(int, input().split())))
dictA = {}
res = 0
for i in range(N):
    dictA.setdefault(List[i], 0)
    dictA[List[i]] += 1
    res += List[i]
num = 0
for i in range(Row):
    if QList[i][0] not in dictA:
        pass
    else:
        num = dictA[QList[i][0]]
        res = res - dictA[QList[i][0]] * QList[i][0]
        dictA[QList[i][0]] = 0
        dictA.setdefault(QList[i][1], 0)
        dictA[QList[i][1]] += num
        res += QList[i][1] * num
    print(res)
