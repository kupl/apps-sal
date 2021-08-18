class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        def helper(arr, limit):
            from collections import deque
            Q = deque()
            Q_2 = deque()
            result = 0
            if len(nums) == 1:
                return 1
            for i in range(len(arr)):
                v = arr[i]
                while len(Q) and abs(v - Q[0][1]) > limit:
                    j, _ = Q.popleft()

                while len(Q_2) and abs(v - Q_2[0][1]) > limit:
                    j, _ = Q_2.popleft()

                if len(Q) and len(Q_2):
                    r = i - max(Q[0][0], Q_2[0][0]) + 1
                    result = max(result, r)

                ni = i
                while len(Q) and v <= Q[-1][1]:
                    mp, vp = Q.pop()
                    if abs(vp - v) <= limit:
                        ni = mp
                Q.append((ni, v))
                ni = i
                while len(Q_2) and v >= Q_2[-1][1]:
                    mp, vp = Q_2.pop()
                    if abs(vp - v) <= limit:
                        ni = mp
                Q_2.append((ni, v))

            return result

        r1 = helper(nums, limit)

        return r1
