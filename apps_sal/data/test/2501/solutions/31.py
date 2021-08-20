from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
constS = defaultdict(int)
constD = defaultdict(int)
for i in range(N):
    Ss = i + A[i]
    Dd = i - A[i]
    constS[Ss] += 1
    constD[Dd] += 1
ans = 0
for (key, val) in constS.items():
    ans += val * constD[key]
print(ans)
