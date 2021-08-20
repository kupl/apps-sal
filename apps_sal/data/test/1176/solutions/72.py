N = int(input())
lsA = map(int, input().split())
mainasu = 0
minabs = 10 ** 10
ls2 = []
for i in lsA:
    if i < 0:
        mainasu += 1
        ls2.append(-i)
    else:
        ls2.append(i)
    minabs = min(minabs, abs(i))
if mainasu % 2 == 0:
    print(sum(ls2))
else:
    print(sum(ls2) - 2 * minabs)
