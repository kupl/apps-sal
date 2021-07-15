class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        length = [0] * (len(arr)+2)
        count = [0] * (len(arr)+1)
        ans = -1
        for i, a in enumerate(arr):
            left, right = length[a-1], length[a+1]
            length[a] = length[a-left] = length[a+right] = left + right + 1
            count[left] -= 1
            count[right] -= 1
            count[length[a]] += 1
            # print(length, count)
            if count[m]:
                ans = i + 1
        return ans
