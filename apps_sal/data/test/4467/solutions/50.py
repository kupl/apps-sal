from collections import deque
N = int(input())
start = 0
end = 2 * N + 1
R = {}
B = {}
ad_matrix = [[0] * (2 * N + 2) for i in range(2 * N + 2)]
ad_dict = {}
ad_dict[start] = []
ad_dict[end] = []
for n in range(N):
    R[n + 1] = list(map(int, input().split()))
    ad_dict[n + 1] = []
for n in range(N):
    B[N + n + 1] = list(map(int, input().split()))
    ad_dict[N + n + 1] = []
for r_ in R.keys():
    ad_dict[start].append(r_)
    ad_dict[r_].append(start)
for b_ in B.keys():
    ad_dict[end].append(b_)
    ad_dict[b_].append(end)
for r_ in R.keys():
    ad_matrix[start][r_] = 1
    r = R[r_]
    for b_ in B.keys():
        ad_matrix[b_][end] = 1
        b = B[b_]
        if r[0] < b[0] and r[1] < b[1]:
            ad_matrix[r_][b_] = 1
            ad_dict[r_].append(b_)
ans = 0
while True:
    start = 0
    end = 2 * N + 1
    color = {}
    for n in range(end + 1):
        color[n] = -1
    visit = deque([start])
    color[start] = 0
    while visit:
        start = visit[-1]
        for v in ad_dict[start]:
            if color[v] == -1:
                visit.append(v)
                color[v] = 0
                break
        else:
            visit.pop()
            color[start] = 1
        if color[end] == 0:
            visit = list(visit)
            flow = 10 ** 10
            for (d1, d2) in zip(visit[:-1], visit[1:]):
                flow = min(flow, ad_matrix[d1][d2])
            for (d1, d2) in zip(visit[:-1], visit[1:]):
                ad_matrix[d1][d2] -= flow
                ad_matrix[d2][d1] += flow
                if ad_matrix[d1][d2] <= 0:
                    ad_dict[d1].remove(d2)
                    ad_dict[d2].append(d1)
            break
    if not visit:
        break
    ans += 1
print(ans)
