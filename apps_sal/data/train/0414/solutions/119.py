class Solution:
    #给定不相同元素数组，比较数组中前两个元素，赢得留下，输的放到数组最后，求出最先赢k轮的数字
    #解法：当遍历数组一遍后，还不能得到结果，就只可能是数组最大值了；因此只要维护一个当前最大值变量，连续k次不变即为结果
    def getWinner(self, arr: List[int], k: int) -> int:
        max_temp = arr[0]
        rounds = 0
        for i in range(1, len(arr)):
            if arr[i] > max_temp:
                rounds = 1
                max_temp = arr[i]
            else:
                rounds += 1
            if rounds == k:
                return max_temp
        return max(arr)
