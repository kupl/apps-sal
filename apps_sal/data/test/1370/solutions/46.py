def main():
    import sys
    sys.setrecursionlimit(10**9)
    input = sys.stdin.readline
    INF = 10**9

    H, W, K = map(int, input().split())
    chocolate = [ input()[:-1] for _ in range(H) ]
    
    loop_H = range(H)
    loop_W = range(W)
    min_cut = INF-1
    for div in range(1 << (H-1)):
        # 横割りでグループ分け
        group = [[]]
        group_number = 0
        for i in loop_H:
            group[group_number].append(i)
            if div >> i & 1:
                group.append([])
                group_number += 1
        # 縦に切っていく
        cut = group_number
        zeros = [0] * len(group)
        cnt = zeros.copy()
        w = 0
        while w < W:
            now = zeros.copy()
            for g in range(len(group)):
                for i in group[g]:
                    if chocolate[i][w] == '1':
                        now[g] += 1
                if now[g] > K:
                    cut = INF
                    break
                if cnt[g] + now[g] > K:
                    cut += 1
                    w -= 1
                    cnt = zeros.copy()
                    break
                cnt[g] += now[g]
            w += 1
        if cut < min_cut:
            min_cut = cut
    print(min_cut)

main()
