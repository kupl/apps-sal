import heapq as hq

n, k = map(int, input().split())
A = []
S0 = []  # 種類が増えない寿司
S1 = []  # 種類が増える寿司
for i in range(n):
    t, d = map(int, input().split())
    A.append([t, d])
A = list(reversed(sorted(A)))

now = 0
for i in range(n):
    t = A[i][0]
    d = A[i][1]
    if now == t:
        S0.append(-d)
    else:
        S1.append(-d)
        now = t
hq.heapify(S0)
hq.heapify(S1)
C = []  # 消し得る寿司のストック(S0から出したもの)

x = 0  # おいしさの合計
y = 0  # 種類数
for i in range(k):
    if len(S0) == 0:
        x += -hq.heappop(S1)
        y += 1
        continue
    if len(S1) == 0:
        s0 = -hq.heappop(S0)
        x += s0
        hq.heappush(C, s0)
        continue
    if S1[0] <= S0[0]:
        x += -hq.heappop(S1)
        y += 1
    else:
        s0 = -hq.heappop(S0)
        x += s0
        hq.heappush(C, s0)
ans = x + y**2

for i in range(min(len(S1), len(C))):
    c = hq.heappop(C)
    s1 = -hq.heappop(S1)
    x += s1 - c
    y += 1
    ans = max(x + y**2, ans)
print(ans)
