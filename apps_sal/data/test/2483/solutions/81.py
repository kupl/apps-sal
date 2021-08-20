import sys
sys.setrecursionlimit(10 ** 6)
(N, C) = list(map(int, input().split()))
C = 30
st = [[] for i in range(C)]
for i in range(N):
    (s, t, c) = list(map(int, input().split()))
    st[c - 1].append((s - 1, t - 1))
data = [0] * (10 ** 5 * 2)
for i in range(C):
    data_tmp = [0] * (10 ** 5 * 2)
    for j in range(len(st[i])):
        (s, t) = st[i][j]
        start = max(s * 2, 0)
        end = min((t - 1) * 2 + 1, 10 ** 5 * 2 - 1)
        data_tmp[start] += 1
        data_tmp[end + 1] -= 1
    for j in range(1, len(data_tmp) - 1):
        if data_tmp[j] > 0:
            data_tmp[j - 1] += data_tmp[j]
            data_tmp[j] = 0
    for j in range(0, len(data_tmp)):
        data[j] += data_tmp[j]
ans = [data[0]]
for i in range(1, len(data)):
    ans.append(ans[-1] + data[i])
print(max(ans))
