n = int(input())
data = []
for i in range(n):
    temp = [int(x) for x in input().split()]
    data.append(temp)

answer = []
for i in range(n):
    carGood = True
    for j in range(n):
        if data[i][j] == 1 or data[i][j] == 3:
            carGood = False
            break
    if carGood:
        answer.append(str(i + 1))

if len(answer) == 0:
    print(0)
    return
print(len(answer))
print(" ".join(answer))

