n = int(input())
stairs = list(map(int, input().split()))
count = 1
lenst = []
for i in range(len(stairs)):
    if i != 0 and stairs[i] == 1:
        count += 1
        lenst.append(stairs[i - 1])
lenst.append(stairs[-1])
print(count)
print(*lenst)

