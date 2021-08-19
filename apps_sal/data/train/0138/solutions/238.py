class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums))]
        res = 0
        if nums[0] > 0:
            dp[0][0] = 1
        elif nums[0] < 0:
            dp[0][1] = 1
        res = max(res, dp[0][0])
        for idx in range(1, len(nums)):
            if nums[idx] == 0:
                (dp[idx][0], dp[idx][1]) = (0, 0)
            elif nums[idx] > 0:
                dp[idx][0] = dp[idx - 1][0] + 1
                if dp[idx - 1][1] > 0:
                    dp[idx][1] = dp[idx - 1][1] + 1
                res = max(dp[idx][0], res)
            elif nums[idx] < 0:
                dp[idx][1] = dp[idx - 1][0] + 1
                if dp[idx - 1][1] > 0:
                    dp[idx][0] = dp[idx - 1][1] + 1
                res = max(res, dp[idx][0])
        return res


'\nclass Solution:\n    def getMaxLen(self, nums: List[int]) -> int:\n        diction = {}\n        diction["pos"], diction["neg"] = 0, 0\n        prevpos, prevneg = 0, 0\n        res = 0\n        for num in nums:\n            if num == 0:\n                diction["pos"], diction["neg"] = 0, 0\n                prevpos, prevneg = 0, 0\n            elif num > 0:\n                diction["pos"] += 1\n                if diction["neg"] % 2 == 0:\n                    res = max(res, diction["pos"]+diction["neg"]+prevpos)\n                    print(num, res)\n                else:\n                    res = max(res, diction["pos"], prevpos)\n        \n            elif num < 0:\n                diction["neg"] += 1\n                print("neg", num, diction["neg"], diction["pos"], prevpos)\n                if diction["neg"] % 2 == 1:\n                    res = max(res, diction["pos"])\n                    prevpos += diction["pos"]\n                    diction["pos"] = 0\n                else:\n                    res = max(res, diction["pos"]+diction["neg"]+prevpos)\n                    prevpos = diction["neg"] + diction["pos"] + prevpos\n                    diction["neg"] = 0\n                    diction["pos"] = 0\n                    \n        print(res)\n        return res\n'
'\n        diction = {}\n        diction["pos"], diction["neg"] = 0, 0\n        res = 0\n        for num in nums:\n            if num == 0:\n                diction["pos"], diction["neg"] = 0, 0\n            elif num > 0:\n                diction["pos"] += 1\n                if diction["neg"] % 2 == 0:\n                    res = max(res, diction["pos"]+diction["neg"])\n            elif num < 0:\n                diction["neg"] += 1\n                \n                if diction["neg"] % 2 == 1:\n                    res = max(res, diction["pos"]+diction["neg"]-1)\n                else:\n                    res = max(res, diction["pos"]+diction["neg"])\n                \n        print(res)\n        \n        return res\n        \n\n'
