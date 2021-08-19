class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        _max = max(worker) + 1
        make = [0] * _max
        num = [(difficulty[i], profit[i]) for i in range(len(profit)) if difficulty[i] < _max]
        num.sort(key=lambda x: x[0])
        p_max = 0
        for i in range(len(num)):
            p_max = max(p_max, num[i][1])
            if num[i][1] >= p_max:
                make[num[i][0]] = num[i][1]
        pre = -1
        for i in range(len(make)):
            if make[i] != 0:
                pre = make[i]
            elif pre != -1:
                make[i] = pre
        ans = 0
        for w in worker:
            ans += make[w]
        return ans
