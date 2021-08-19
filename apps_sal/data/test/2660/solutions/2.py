import heapq


def main():
    Q = int(input())
    query_list = [list(map(int, input().split(' '))) for _ in range(Q)]
    # fの最小を与えるxの計算用
    que_left, que_right = [], []  # 最大ヒープと最小ヒープ
    # fの最小値の計算用
    sum_a_cost = 0
    sum_b = 0
    for query in query_list:
        if query[0] == 1:
            a, b = query[1], query[2]
            # fの更新
            if len(que_right) - len(que_left) == 1:
                sum_a_cost += abs(a - que_right[0])
            elif 0 < len(que_left) == len(que_right):
                if a > que_right[0]:
                    sum_a_cost += a - que_right[0]
                elif a < - que_left[0]:
                    sum_a_cost += - que_left[0] - a
            sum_b += b
            # xの更新
            if len(que_right) == 0 or a >= que_right[0]:
                heapq.heappush(que_right, a)
            else:
                # 最大ヒープにするため符号反転
                heapq.heappush(que_left, - a)
            # ヒープのサイズ差が0 or 1になるよう調整
            if len(que_right) - len(que_left) == - 1:
                heapq.heappush(que_right, - heapq.heappop(que_left))
            elif len(que_right) - len(que_left) == 2:
                heapq.heappush(que_left, - heapq.heappop(que_right))
        else:
            x = que_right[0] if len(que_right) - len(que_left) == 1 else (- que_left[0])
            f = sum_a_cost + sum_b
            print('{} {}'.format(x, f))


def __starting_point():
    main()


__starting_point()
