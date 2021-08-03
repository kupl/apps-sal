n = int(input())
a = list(map(int, input().split()))
INF = 10 ** 20
DP = [-INF] * 12
DP[1] = a[0]
DP[5] = -a[0]
for elem in a[1:]:
    newDP = []
    newDP.append(DP[5] + elem)
    newDP.append(DP[3] + elem)
    newDP.append(DP[4] + elem)
    newDP.append(DP[1] - elem)
    newDP.append(DP[2] - elem)
    newDP.append(DP[0] - elem)
    newDP.append(max(DP[2] + elem, DP[8] + elem, DP[11] + elem))
    newDP.append(max(DP[0] + elem, DP[6] + elem, DP[9] + elem))
    newDP.append(max(DP[1] + elem, DP[7] + elem, DP[10] + elem))
    newDP.append(max(DP[4] - elem, DP[7] - elem, DP[10] - elem))
    newDP.append(max(DP[5] - elem, DP[8] - elem, DP[11] - elem))
    newDP.append(max(DP[3] - elem, DP[6] - elem, DP[9] - elem))
    DP = newDP
if n == 1:
    print(a[0])
else:
    print(max(DP[7], DP[10]))
