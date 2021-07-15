class Solution:
    # hashmap
    # review
    def maxEqualFreq(self, nums: List[int]) -> int:
        count = collections.defaultdict(int)
        freq = collections.defaultdict(int)

        # for test case [1,1,1,2,2,2] , the ans is 5, [1,1,1,2,2], len=5, you can remove 1, then 1 and 2 occur 2 times
        # we will get count {1:3, 2:3}
        # for freq: we would get {1:2, 2:2, 3: 2}, notice we loop from left to right, so we would get
        # freq : {1:1}, {1:1, 2:1}, {1:1,2:1,3:1}, {1:2,2:1,3:1}, {1:2,2:2,3:1},{1:2,2:2,3:2}
        for n in nums:
            count[n] += 1
            freq[count[n]] += 1

        for i in range(len(nums) - 1, 0, -1):
            # 2 case, case 1 , keep i, then you have to remove another on from 0 -- i-1
            # for test case [1,1,1,2,2,2], at index i = 5, 3 * 2 = 6 != 5, because we need to remove one element if we
            # want to keep ith element
            # but i = 4,  count[2] = 2, freq[2] = 2, 2 * 2 = 4, ie, when i = 4, total 5 elements, remove 1 ele, remain 4.
            # notice we need to return ri+1, because w need to prefix length, which include the removed element

            # this means from 0->i , each num appear equal times, then we just need to remove i+1
            if count[nums[i]] * freq[count[nums[i]]] == i:
                return i + 1
            freq[count[nums[i]]] -= 1
            count[nums[i]] -= 1

            if count[nums[i - 1]] * freq[count[nums[i - 1]]] == i:
                return i + 1

        return 1



