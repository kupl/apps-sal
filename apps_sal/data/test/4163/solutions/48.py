n = int(input())
dList = []
count = 0
s = 'No'
for i in range(n):
    d = []
    (d1, d2) = list(map(int, input().split()))
    d.append(d1)
    d.append(d2)
    dList.append(d)
for i in range(n - 2):
    if dList[i][0] == dList[i][1] and dList[i + 1][0] == dList[i + 1][1] and (dList[i + 2][0] == dList[i + 2][1]):
        s = 'Yes'
        break
print(s)
