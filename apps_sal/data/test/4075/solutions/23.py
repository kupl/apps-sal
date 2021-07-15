def abc128_c():
    # n個のスイッチ、m個の電球
    N, M = list(map(int, input().split()))

    connected_switches = []
    for i in range(M):
        # [k, s1, s2, ...sn][1:]
        tmp = list(map(int, input().split()))[1:]
        connected_switches.append(tmp)

    p = list(map(int, input().split()))

    ans = 0

    # スイッチの状態(ON/OFF)をbitですべて列挙する
    for i in range(2 ** N):
        # 各電球が点灯しているかをチェックする
        for j in range(M):
            on_switch_count = 0
            # スイッチがつながっていて、かつ、onになっているものをカウント
            for k in range(N):
                # connected_switches[j]には[s1, s2, ...]が入っているため+1が必要
                if k + 1 in connected_switches[j] and ((i >> k) & 1):
                    on_switch_count += 1

            # 電灯をチェックして一つでもついていないものがあればそのスイッチの状態ではすべての電灯が付くという条件を満たせない
            if on_switch_count % 2 != p[j]:
                break
            
            if j == (M - 1):
                ans += 1

    print(ans)

def __starting_point():
    abc128_c()

__starting_point()
