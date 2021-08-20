def est_time(sta, N, csf_list):
    SUM = 0
    for i in range(sta, N):
        if i == sta:
            SUM += csf_list[i - 1][0] + csf_list[i - 1][1]
        elif SUM >= csf_list[i - 1][1]:
            SUM = (SUM + csf_list[i - 1][2] - 1) // csf_list[i - 1][2] * csf_list[i - 1][2]
            SUM += csf_list[i - 1][0]
        else:
            SUM = csf_list[i - 1][1]
            SUM += csf_list[i - 1][0]
    return SUM


N = int(input())
csf_list = [tuple(map(int, input().split())) for _ in range(N - 1)]
for i in range(N):
    print(est_time(i + 1, N, csf_list))
