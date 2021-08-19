n = int(input())
myList = []
for k in range(0, n):
    myList.append(0)
counter = 0
for i in range(0, n - 1):
    (a, b) = list(map(int, input().split()))
    myList[a - 1] += 1
    myList[b - 1] += 1
for j in range(0, len(myList)):
    if myList[j] == 1:
        counter += 1
print(counter)
