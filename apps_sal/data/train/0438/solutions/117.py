class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        # 两个数组，一个记录长度，另一个记录长度的个数
        length = [0 for _ in range(len(arr) + 2)]
        count = [0 for _ in range(len(arr) + 1)]
        res = -1
        for i, a in enumerate(arr):
            # 先把左边的长度和右边的1长度取出来
            left, right = length[a - 1], length[a + 1]
            # 现在这个位置的长度就是左边的长度加上右边的长度加上自己
            # 距离a位置的左右两边的边角处的索引也会被附上新的值，之后的计算可能用得上
            length[a] = length[a - left] = length[a + right] = left + right + 1

            # 然后就是更新count了
            count[left] -= 1
            count[right] -= 1
            count[length[a]] += 1

            # 判断m是否还存在，只要m存在那就是满足条件的最后一步
            if count[m]:
                res = i + 1
        return res
