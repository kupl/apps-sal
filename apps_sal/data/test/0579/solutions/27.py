# import numpy as np
import itertools


def __starting_point():

    N, K = list(map(int, input().split()))
    P = [int(p) - 1 for p in input().split()]
    C = list(map(int, input().split()))

    # print(P)
    # 一度計算したサイクル情報をキャッシュしておくための配列
    # cycleIDs = np.full( N, -1, np.int64 )
    cycleIDs = [-1 for _ in range(N)]
    cycleInfs = []
    cycleID = 0
    procCnt = 0

    for n in range(N):
        v = n

        if cycleIDs[v] != -1:
            continue
        else:
            currentCycleCosts = []
            while True:
                # 全頂点について、属するサイクルを計算する
                currentCycleCosts.append(C[v])
                cycleIDs[v] = cycleID

                v = P[v]
                if cycleIDs[v] != -1:
                    # サイクル終了
                    # ループを含めない最大の処理回数
                    procCnt = K % len(currentCycleCosts)
                    # それで足りてるのかわからないが、Last2周分は、ループ合計がプラスでも必ずしもループするとは限らない
                    # その部分は、ちゃんと計算する
                    # -------------------------------------------------
                    # 4 101
                    # 2 3 4 1
                    # 50 -49 -50 50
                    # 上記のようなパターンの場合、
                    # 最大25回ループ + 1回処理可能だが、その場合、25 + 50 = 75
                    # 24回ループ + 2回処理でやめると、124になる
                    # 無条件でループする回数は、ループ可能な最大の回数-1らしい
                    # -------------------------------------------------
                    # 割り切れて、尚且つサイクル合計がマイナスのパターンで、最低１個は処理するのにもここで対応
                    if len(currentCycleCosts) + procCnt <= K:
                        procCnt += len(currentCycleCosts)

                    cycleInfs.append((procCnt, len(currentCycleCosts), currentCycleCosts * 3))
                    cycleID += 1
                    break

    # scores = []
    # procCnt = 0
    ans = -10 ** 9
    for procCnt, currentCycleSize, currentCycleCosts in cycleInfs:

        # サイクル内でループしてスコアを稼ぐ場合の考慮
        loopScore = 0
        if sum(currentCycleCosts) > 0:
            cycleLoopCnt = (K - procCnt) // currentCycleSize
            loopScore = cycleLoopCnt * sum(currentCycleCosts[:currentCycleSize])
            # print("loopScore",loopScore,procCnt)

        # このサイクルに属する全頂点分をまとめて計算する
        for i in range(currentCycleSize):
            # print(np.roll( currentCycleCosts, i ).cumsum()[:procCnt])
            ans = max(ans, max(itertools.accumulate(currentCycleCosts[i:i + procCnt])) + loopScore)

    print(ans)
    # print(max(scores))


__starting_point()
