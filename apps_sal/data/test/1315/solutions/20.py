#E - Happy Line
import sys
nLine = int(input())
nMoney = list(map(int, input().split()))
invariante = []
for i in range(len(nMoney)):
    invariante.append(nMoney[i] + i)
invariante.sort()

res = [0] * nLine
for i in range(nLine):
        res[i] = invariante[i] - i
for i in range(nLine - 1):
    if res[i] > res[i+1]:
        print(':(')
        return
print(*res)
