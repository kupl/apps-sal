class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        '''
        https://leetcode.com/problems/longest-arithmetic-sequence/discuss/274611/JavaC++Python-DP
        dp[diff][index] + 1 equals to the length of arithmetic sequence at index with difference diff.
        '''
        '''
        Input: [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.
Input: [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].
Input: [20,1,15,3,10,5,8]
Output: 4
Explanation: 
The longest arithmetic subsequence is [20,15,10,5].
        '''
        '''
Input: [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.
        defaultdict(<class 'int'>, {})
defaultdict(<class 'int'>, {(3, 0): 0, (3, 1): 1})
defaultdict(<class 'int'>, {(3, 0): 0, (3, 1): 1, (6, 0): 0, (6, 2): 1})
defaultdict(<class 'int'>, {(3, 0): 0, (3, 1): 1, (6, 0): 0, (6, 2): 1, (9, 0): 0, (9, 3): 1})
defaultdict(<class 'int'>, {(3, 0): 0, (3, 1): 1, (6, 0): 0, (6, 2): 1, (9, 0): 0, (9, 3): 1, (3, 2): 2})
defaultdict(<class 'int'>, {(3, 0): 0, (3, 1): 1, (6, 0): 0, (6, 2): 1, (9, 0): 0, (9, 3): 1, (3, 2): 2, (6, 1): 0, (6, 3): 1})
defaultdict(<class 'int'>, {(3, 0): 0, (3, 1): 1, (6, 0): 0, (6, 2): 1, (9, 0): 0, (9, 3): 1, (3, 2): 2, (6, 1): 0, (6, 3): 1, (3, 3): 3})
      '''

        '''
        Input:
[24,13,1,100,0,94,3,0,3]
Output:
3
Expected:
2
        '''
        '''
        Input:
[0,8,45,88,48,68,28,55,17,24]
Output:
4
Expected:
2
        '''

        '''Len = len(A)
        res = 0
        for i in range(aLen):
            for j in range(i+1, aLen):
                diff = A[j]-A[i]
                target = A[j] + diff 
                count = 2 
                idx = j+1
                while idx < aLen:
                    if A[idx] == target:
                        count += 1
                        target = target + diff 
                    idx += 1
                res = max(res, count)
        return res'''

        '''aLen =len(A)
        res = 0 
        dp = [{} for _ in range(aLen)]
        for i in range(aLen):
            for j in range(i):
                diff = A[i]-A[j]
                if diff in dp[j]:
                    dp[i][diff] = 1 + dp[j][diff]
                else:
                    dp[i][diff] = 2
                res = max(res, dp[i][diff])
        return res '''

        '''aLen = len(A)
        res = 0 
        dp = [{} for _ in range(aLen)]
        for i in range(aLen):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in dp[j]:
                    dp[i][diff] = 1+ dp[j][diff]
                else:
                    dp[i][diff] = 2 
                res = max(res, dp[i][diff])
        return res '''

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

        '''
        nums_map = {}
        for i,n in enumerate(A):
            nums_map[n] = nums_map.get(n, [])
            nums_map[n].append(i)
        max_length = 2
        for i, n in enumerate(A):
            for j in range(i+1, len(A)):
                m = A[j]
                target = m + (m-n)
                length = 2
                last_index = j
                found = True
                while target in nums_map and found:
                    found = False
                    for index in nums_map[target]:
                        if index > last_index:
                            last_index = index
                            length += 1
                            target += m-n
                            max_length = max(max_length, length)
                            found = True
                            break
                    if not found:
                        break
        return max_length'''
