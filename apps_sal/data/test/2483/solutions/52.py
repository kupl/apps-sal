import numpy as np


def main():
    with open(0) as f:
        N, C = list(map(int, f.readline().split()))
        Rec = [tuple(map(int, f.readline().split())) for _ in range(N)]

    time_line_by_channel = np.array([[0] * (10**5 + 1) for _ in range(C + 1)])
    # チャンネルごとにタイムラインを作成
    for s, t, c in Rec:
        time_line_by_channel[c, s - 1:t] = 1
    # タイムライン結合
    joined_timeline = np.sum(time_line_by_channel, axis=0)
    ans = max(joined_timeline)
    print(ans)


main()
