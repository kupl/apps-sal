# coding: utf-8

import bisect

A, B, Q = map(int, input().split())
*S, = [int(input()) for _ in range(A)]
*T, = [int(input()) for _ in range(B)]
*X, = [int(input()) for _ in range(Q)]

for x in X:
    # 2分探索で、「現在地」と神社群の位置関係を探る
    sx = bisect.bisect(S, x)
    # 現在地から見て東側で最も近い神社
    try:
        se = S[sx]
    except:
        # 東側に存在しない場合は、神社群の中での最東
        se = S[-1]
    # 現在地から見て西側で最も近い神社
    try:
        sw = S[sx - 1]
    except:
        # 西側に存在しない場合は、神社群の中での最西
        sw = S[0]

    tx = bisect.bisect(T, x)
    # 現在地から見て東側で最も近いお寺
    try:
        te = T[tx]
    except:
        # 東側に存在しない場合は、お寺群の中での最東
        te = T[-1]
    # 現在地から見て西側で最も近いお寺
    try:
        tw = T[tx - 1]
    except:
        # 西側に存在しない場合は、お寺群の中での最西
        tw = T[0]

    # 候補 (8通り) をシミュレーション
    # 東神社 -> 東寺
    # 東寺 -> 東神社
    # 東神社 -> 西寺
    # 西寺 -> 東神社
    # 西神社 -> 東寺
    # 東寺 -> 西神社
    # 西神社 -> 西寺
    # 西寺 -> 西神社
    routes = []
    for s in [se, sw]:
        for t in [te, tw]:
            routes.append(abs(s - x) + abs(t - s))
            routes.append(abs(t - x) + abs(s - t))

    # 最小距離を選ぶ
    print(min(routes))
