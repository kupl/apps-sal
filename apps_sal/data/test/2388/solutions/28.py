# 解説放送
# https://atcoder.jp/contests/abc158/submissions/10643692
# dfsの代わりに親の頂点番号を配列で管理する方法
# PyPyでは通った

def main():
    from collections import deque, namedtuple
    from operator import attrgetter
    import sys
    input = sys.stdin.readline

    MOD = 998244353

    Robot = namedtuple('Robot', 'x d reach ind')

    N = int(input())

    robots = []
    for ind in range(N):
        X, D = list(map(int, input().split()))
        robots.append(Robot(X, D, X + D, ind))
    robots.sort(key=attrgetter('x'), reverse=True)

    parents = [-1] * N
    to_candidates = deque()
    for robot_from in robots:  # x降順
        """
        右端に位置するロボットから順に「起点」と見なしていく
        既出のロボットで有向辺の行き先として一度も設定されていないものが
        to_candidatesにx昇順で溜められている
        to_candidatesに含まれるロボットで「起点」から接触範囲内のものがある限り、
        「起点」から有向辺を張り続ける
        to_candidatesの先頭候補(最も左側に位置する)に対して辺を張れない場合、
        それ以降の候補のxはより遠い座標で辺を張れないので
        「起点」から張れる辺がないとわかる
        すべてのロボットは「起点」から辺を張られてto_candidatesから外れるか
        to_candidatesに残り、グラフ(森)の各木のrootとなる
        """
        while to_candidates:
            robot_to = to_candidates[0]
            if robot_to.x < robot_from.reach:
                parents[robot_to.ind] = robot_from.ind
                to_candidates.popleft()
            else:
                break

        to_candidates.appendleft(robot_from)

    ret = 1
    count = [1] * N
    for robot in robots:  # x降順
        par = parents[robot.ind]
        count[robot.ind] += 1
        if ~par:
            count[par] = (count[par] * count[robot.ind]) % MOD
        else:
            ret = (ret * count[robot.ind]) % MOD
            # x降順で見ているのでpar==-1のrootのrobotを見る頃には
            # rootの子は全て見ているので安心してretにかけられる
    print(ret)
    return


def __starting_point():
    main()


__starting_point()
