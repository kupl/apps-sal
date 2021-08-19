import sys
if False:
    inp = open('B.txt', 'r')
else:
    inp = sys.stdin
data = [[] for i in range(100009)]
spines = [0 for i in range(100009)]
dp = [1 for i in range(100009)]
(n, m) = list(map(int, inp.readline().split()))
for i in range(m):
    (a, b) = list(map(int, inp.readline().split()))
    if a < b:
        data[b].append(a)
    else:
        data[a].append(b)
    spines[a] += 1
    spines[b] += 1
ans = 0
dp[1] = 1
ans = spines[1]
for i in range(2, n + 1):
    ret = 0
    for item in data[i]:
        ret = max(ret, dp[item])
    dp[i] = ret + 1
    ans = max(ans, (ret + 1) * spines[i])
print(ans)
