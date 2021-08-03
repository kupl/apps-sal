class Solution:
    # 1599
    def minOperationsMaxProfit(self, customers: 'List[int]', board: int, run: int) -> int:
        waiting = 0
        curr, best, rotate = 0, -math.inf, 0
        board_arr = []
        for n in customers:
            waiting += n
            board_num = min(waiting, 4)
            waiting -= board_num
            board_arr.append(board_num)
        if waiting:
            board_arr += [4] * (waiting // 4)
            board_arr.append(waiting % 4)

        for i, n in enumerate(board_arr):
            curr = curr + n * board - run
            if curr > best:
                best = curr
                rotate = i
        return rotate + 1 if best > 0 else -1
