class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        """
        https://leetcode.com/problems/longest-arithmetic-sequence/discuss/274611/JavaC++Python-DP
        dp[diff][index] + 1 equals to the length of arithmetic sequence at index with difference diff.
        """
        '\n        Input: [3,6,9,12]\nOutput: 4\nExplanation: \nThe whole array is an arithmetic sequence with steps of length = 3.\nInput: [9,4,7,2,10]\nOutput: 3\nExplanation: \nThe longest arithmetic subsequence is [4,7,10].\nInput: [20,1,15,3,10,5,8]\nOutput: 4\nExplanation: \nThe longest arithmetic subsequence is [20,15,10,5].\n        '
        "\nInput: [3,6,9,12]\nOutput: 4\nExplanation: \nThe whole array is an arithmetic sequence with steps of length = 3.\n        defaultdict(<class 'int'>, {})\ndefaultdict(<class 'int'>, {(3, 0): 0, (3, 1): 1})\ndefaultdict(<class 'int'>, {(3, 0): 0, (3, 1): 1, (6, 0): 0, (6, 2): 1})\ndefaultdict(<class 'int'>, {(3, 0): 0, (3, 1): 1, (6, 0): 0, (6, 2): 1, (9, 0): 0, (9, 3): 1})\ndefaultdict(<class 'int'>, {(3, 0): 0, (3, 1): 1, (6, 0): 0, (6, 2): 1, (9, 0): 0, (9, 3): 1, (3, 2): 2})\ndefaultdict(<class 'int'>, {(3, 0): 0, (3, 1): 1, (6, 0): 0, (6, 2): 1, (9, 0): 0, (9, 3): 1, (3, 2): 2, (6, 1): 0, (6, 3): 1})\ndefaultdict(<class 'int'>, {(3, 0): 0, (3, 1): 1, (6, 0): 0, (6, 2): 1, (9, 0): 0, (9, 3): 1, (3, 2): 2, (6, 1): 0, (6, 3): 1, (3, 3): 3})\n      "
        '\n        Input:\n[24,13,1,100,0,94,3,0,3]\nOutput:\n3\nExpected:\n2\n        '
        '\n        Input:\n[0,8,45,88,48,68,28,55,17,24]\nOutput:\n4\nExpected:\n2\n        '
        'Len = len(A)\n        res = 0\n        for i in range(aLen):\n            for j in range(i+1, aLen):\n                diff = A[j]-A[i]\n                target = A[j] + diff \n                count = 2 \n                idx = j+1\n                while idx < aLen:\n                    if A[idx] == target:\n                        count += 1\n                        target = target + diff \n                    idx += 1\n                res = max(res, count)\n        return res'
        'aLen =len(A)\n        res = 0 \n        dp = [{} for _ in range(aLen)]\n        for i in range(aLen):\n            for j in range(i):\n                diff = A[i]-A[j]\n                if diff in dp[j]:\n                    dp[i][diff] = 1 + dp[j][diff]\n                else:\n                    dp[i][diff] = 2\n                res = max(res, dp[i][diff])\n        return res '
        'aLen = len(A)\n        res = 0 \n        dp = [{} for _ in range(aLen)]\n        for i in range(aLen):\n            for j in range(i):\n                diff = A[i] - A[j]\n                if diff in dp[j]:\n                    dp[i][diff] = 1+ dp[j][diff]\n                else:\n                    dp[i][diff] = 2 \n                res = max(res, dp[i][diff])\n        return res '
        aLen = len(A)
        res = 0
        dp = [{} for _ in range(aLen)]
        for i in range(aLen):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                res = max(res, dp[i][diff])
        return res
        '\n        #why is this solution the fastest??????\n        nums_map = {}\n        for i,n in enumerate(A):\n            nums_map[n] = nums_map.get(n, [])\n            nums_map[n].append(i)\n        max_length = 2\n        for i, n in enumerate(A):\n            for j in range(i+1, len(A)):\n                m = A[j]\n                target = m + (m-n)\n                length = 2\n                last_index = j\n                found = True\n                while target in nums_map and found:\n                    found = False\n                    for index in nums_map[target]:\n                        if index > last_index:\n                            last_index = index\n                            length += 1\n                            target += m-n\n                            max_length = max(max_length, length)\n                            found = True\n                            break\n                    if not found:\n                        break\n        return max_length'
