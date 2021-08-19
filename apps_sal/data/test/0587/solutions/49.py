from heapq import heapify, heappush, heappop
(N, K) = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]
S.sort(key=lambda x: -x[1])
types = set()
RS = []
AS = []
d_sum = 0
for i in range(K):
    (_type, value) = (S[i][0], S[i][1])
    if _type in types:
        heappush(RS, (value, _type))
    else:
        types.add(_type)
    d_sum += value
t_sum = len(types)
d_sum += pow(t_sum, 2)
for i in range(K, N):
    (_type, value) = (S[i][0], S[i][1])
    if not _type in types:
        heappush(AS, (-value, _type))
        types.add(_type)
ans = d_sum
while len(AS) > 0 and len(RS) > 0:
    (av, at) = heappop(AS)
    (rv, rt) = heappop(RS)
    t_sum += 1
    d_sum += -av - rv + pow(t_sum, 2) - pow(t_sum - 1, 2)
    ans = max(ans, d_sum)
print(ans)
