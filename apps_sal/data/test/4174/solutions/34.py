n, X = map(int, input().split())
l = list(map(int, input().split()))

sumList = [0]
for i in range(n):
    s = sumList[i]+l[i]
    if s > X:
        break
    sumList.append(s)

print(len(sumList))
