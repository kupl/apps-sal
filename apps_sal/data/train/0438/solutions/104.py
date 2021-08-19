class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m

        counts = [0] * (len(arr) + 2)
        # m_nums = 0
        ans = -1

        for index, i in enumerate(arr):
            left = counts[i - 1]
            right = counts[i + 1]
            total = 1 + left + right
            counts[i] = total
            counts[i - left] = total
            counts[i + right] = total

            if left == m or right == m:
                ans = index
            # if left==m:
            #     m_nums-=1
            # if right == m:
            #     m_nums-=1
            # if total == m:
            #     m_nums+=1
            # if m_nums >0:
            #     ans = index+1

        return ans
