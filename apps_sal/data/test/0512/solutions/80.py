import sys


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    start = []
    end = []
    confirmed = set()
    confirmed_start = set()
    confirmed_end = set()
    start_set = set()
    end_set = set()
    start_only = set()
    end_only = set()
    ill_input = False
    for _ in range(N):
        (a, b) = list(map(int, input().split()))
        if a != -1:
            a -= 1
        if b != -1:
            b -= 1
        if a != -1 and b != -1 and (a >= b):
            ill_input = True
        if a != -1 and (a in start_set or a in end_set):
            ill_input = True
        if b != -1 and (b in start_set or b in end_set):
            ill_input = True
        start.append(a)
        end.append(b)
        if a != -1:
            start_set.add(a)
        if b != -1:
            end_set.add(b)
        if a != -1 and b == -1:
            start_only.add(a)
        if a == -1 and b != -1:
            end_only.add(b)
        if a != -1 and b != -1:
            confirmed.add((a, b))
            confirmed_start.add(a)
            confirmed_end.add(b)
    if ill_input:
        print('No')
        return
    '\n    重なりがある場合は乗り降りの関係が1ずつずれることに気づく。\n    なので2N個のフロアをうまく偶数区間に区切って、各区間内で乗り降りが\n    1ずつずれる、かつそれが与えられた条件に合うか確認すれば良い。\n\n    これはdpで判定する。\n        dp[i] = (最後にi番目で区切ったとして、そこまでで条件を満たすのが可能か)\n    '
    state = [0] * (N * 2)
    for (s, e) in zip(start, end):
        if s != -1:
            state[s] = 1
        if e != -1:
            state[e] = -1
    ok = [[0] * (N * 2) for _ in range(N * 2)]
    for s in range(N * 2):
        for e in range(s + 1):
            ok[s][e] = -1
    for s in start_only:
        for e in range(s + 1, N * 2):
            if e in confirmed_start or e in confirmed_end or e in end_only or (e in start_set):
                ok[s][e] = -1
    for e in end_only:
        for s in range(e):
            if s in confirmed_start or s in confirmed_end or s in start_only or (s in end_set):
                ok[s][e] = -1
    for s in range(N * 2):
        if s in start_only:
            continue
        for e in range(s + 1, N * 2):
            if e in confirmed_start or e in confirmed_end or e in start_only:
                ok[s][e] = -1
    for e in range(N * 2):
        if e in end_only:
            continue
        for s in range(e):
            if s in confirmed_start or s in confirmed_end or s in end_only:
                ok[s][e] = -1
    for (s, e) in confirmed:
        ok[s][e] = 1
        for ns in range(N * 2):
            if ns != s:
                ok[ns][e] = -1
            ok[ns][s] = -1
        for ne in range(N * 2):
            if ne != e:
                ok[s][ne] = -1
            ok[e][ne] = -1
    dp = [False] * (N * 2 + 1)
    dp[0] = True
    for i in range(2, N * 2 + 1, 2):
        flag = False
        for j in range(i - 2, -1, -2):
            if not dp[j]:
                continue
            stride = (i - j) // 2
            for k in range(j, j + stride):
                if state[k] == -1 or state[k + stride] == 1 or ok[k][k + stride] == -1:
                    break
            else:
                flag = True
                break
        if flag:
            dp[i] = True
    if dp[-1]:
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()
