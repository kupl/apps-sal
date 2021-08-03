import sys
T = int(input())
res = []

for t in range(T):
    N, K = map(int, sys.stdin.readline().split())
    a_list = list(map(int, sys.stdin.readline().split()))
    if N == 1:
        res.append(a_list[0])
        continue
    ans = float("inf")
    ans_i = -1
    for i in range(N - K):
        tmp = abs(a_list[i + K] - a_list[i])
        if ans > tmp:
            ans = tmp
            ans_i = i
    res.append((a_list[ans_i + K] + a_list[ans_i]) // 2)

for r in res:
    print(r)
