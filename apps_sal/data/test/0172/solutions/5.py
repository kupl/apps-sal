n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = [0] * 5
for elem in A:
    cnt[elem - 1] += 1
for elem in B:
    cnt[elem - 1] += 1
bad = 0
for elem in cnt:
    bad += elem % 2
if bad != 0:
    print(-1)
else:
    cntA = [0] * 5
    cntB = [0] * 5
    for elem in A:
        cntA[elem - 1] += 1
    for elem in B:
        cntB[elem - 1] += 1
    ans = 0
    for i in range(5):
        ans += abs(cntA[i] - cntB[i]) // 2
    print(ans // 2)

