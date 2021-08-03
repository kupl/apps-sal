class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:

        index = []

        for i in range(len(nums)):

            if nums[i] == 1:

                index.append(i)

        if not index:

            return True

        if len(index) == 1:

            return True

        print(index)

        for i in range(len(index) - 1):

            print(i)

            if(index[i + 1] - index[i] >= (k + 1)):

                continue

            else:

                return False

        return True
