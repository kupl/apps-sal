class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/discuss/830480/C%2B%2B-O(N)-Sliding-window-Explanation-with-Illustrations
        # 这道题是two pointer类型题目
        # 大体的逻辑就是左边一个pointer，右边一个pointer
        left = 0
        right = len(arr) - 1

        # left向右走，如果left+1指向的数字大于等于left就一直走
        # 如果left一路走到了end，那就说明原list就是sorted的，那就直接return
        while left + 1 <= len(arr) - 1 and arr[left] <= arr[left + 1]:
            left += 1

        if left == right:
            return 0

        # right同理向左走，如果right-1小于等于right就继续走
        while right - 1 >= 0 and arr[right] >= arr[right - 1]:
            right -= 1

        # 然后先处理两边 就是当0到right-1 或者 left+1到end 其中一个去掉，也就是去掉两边
        # 在这种情况下 无论怎么移除中间的部分 都没有办法使两边组合起来成为递增
        # 这种情况就像[6,7,8,9,10,3,5,20,4,1,2,3]
        # left指向10，right指向1 -- 因为只能移除一个subarry所以要从 6到20 和 3到3 中选一个

        # 所以如果是这种case，那就先要计算两个边较小的那个
        # right就是0到right -1 index的长度
        # len(arr)- 1 - left 就是 end - left 也就是 left + 1到end index的长度
        min_sublen = min(right, len(arr) - 1 - left)

        # 然后就可以开始进行中间情况的运算
        # 大概就是在这种情况下我们left和right要进行移动，然后找到最短的中间subarray，使得该array去掉后左右两边能成为递增array
        # 大概的操作就是比较 两个指针lp和rp 从0到left 和 从right到end

        # 如果lp小于rp了，那就说明去掉lp和rp中间范围就是递增，此时就可以计算下subarr长度，然后进行比较，留下最小的那个。然后lp向右移动一位再继续比较
        # 知道lp到达了left，或者rp到达了end，就停止 返回最短的subarry长度
        lp = 0
        rp = right

        # 如果lp大于rp，那就说明lp太大了，rp向右移动一位
        while lp <= left and rp <= len(arr) - 1:
            if arr[lp] > arr[rp]:
                rp += 1
            # 如果lp小于rp了，那就说明去掉lp和rp中间范围就是递增，此时就可以计算下subarr长度，然后进行比较，留下最小的那个。然后lp向右移动一位再继续比较
            else:
                min_sublen = min(min_sublen, rp - lp - 1)
                lp += 1

        return min_sublen
