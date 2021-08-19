class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        # length[i]表示位置i的连续1长度为多长，因为每次都是插入一个新的元素使原本不连通的左右连通
        # 所以对于左边的length[i -1]表示以i-1为结束的连续1长度有多长
        # 对于右边的length[i + 1]表示以i+1为开始的连续1长度有多长
        length = [0] * (len(arr) + 2)
        # count[i]表示长度为i的序列有几个
        count = [0] * (len(arr) + 1)
        res = -1
        for step, i in enumerate(arr):
            left, right = length[i - 1], length[i + 1]
            length[i] = length[i - left] = length[i + right] = left + right + 1
            count[left] -= 1
            count[right] -= 1
            count[length[i]] += 1
            if count[m]:
                res = step + 1
        return res
