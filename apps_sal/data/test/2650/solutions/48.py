# -*- coding:utf-8 -*-

def solve():
    import heapq

    M = 2*(10**5)
    N, Q = list(map(int, input().split()))
    As, Bs = [], []
    yochien = [list() for _ in range(M)]  # 幼稚園
    for i in range(N):
        a, b = list(map(int, input().split()))
        b = b - 1
        As.append(a), Bs.append(b)
        heapq.heappush(yochien[b], (-a, i))  # 幼稚園bに、幼児iのレートaを、プライオリティキューで持つ。（先頭に最も大きいレートの幼児がくるようにする）

    # 各幼稚園のトップコーダー連中の幼児情報を、プライオリティキューtopにぶちこむ。
    # 幼児情報は(レート, 幼児, 所属幼稚園)の形式でぶちこむ
    # すなわち、top[0]にはトップコーダー連中の最低レートの幼児情報が入っている。
    # 「トップコーダー連中の最低レート幼児」は長いので、以降「平等レート幼児」と呼ぶ。
    top = []
    for m in range(M):
        if yochien[m]:
            heapq.heappush(top, (-yochien[m][0][0], yochien[m][0][1], m))

    # クエリを処理する
    for _ in range(Q):
        # 幼児cを幼稚園dに転園させたい
        c, d = list(map(int, input().split()))
        c, d = c-1, d-1

        before = Bs[c]  # 転園前の幼稚園
        Bs[c] = d

        # 幼児cを幼稚園dに転園する
        heapq.heappush(yochien[d], (-As[c], c))

        if yochien[d][0][1] == c:
            # 幼児cが転園先の幼稚園dでトップコーダーになったならば、トップを更新する
            heapq.heappush(top, (As[c], c, d))

        flag = False  # 転園前の幼稚園のトップコーダーが変わったか？
        while yochien[before] and Bs[yochien[before][0][1]] != before:
            # 「転園前の幼稚園が空じゃない」、かつ、「転園前の幼稚園のトップコーダーが変わった」ならば、
            # 転園前の幼稚園のトップコーダーを削除する
            heapq.heappop(yochien[before])
            flag = True

        if flag and yochien[before]:
            # 転園前の幼稚園のトップコーダーが変わってしまい、まだ転園前の幼稚園に幼児が存在するならば、
            # 転園前の幼稚園のトップコーダーはその幼児になる
            heapq.heappush(top, (-yochien[before][0][0], yochien[before][0][1], before))

        while not yochien[top[0][2]] or yochien[top[0][2]][0][1] != top[0][1]:
            # 「平等レート幼児の所属幼稚園が空じゃない」、または、「平等レート幼児が変わった」ならば、
            # 平等レート幼児を更新する
            heapq.heappop(top)

        # 平等さ（平等レート幼児のレート値）を表示する
        print((top[0][0]))


def __starting_point():
    solve()

__starting_point()
