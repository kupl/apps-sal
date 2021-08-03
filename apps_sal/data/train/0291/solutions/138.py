class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        even = [0] * (n)
        odd = [0] * (n)
        # dp, where odd[i], even[i] are numbers of sub arrays that end at i
        # we then sum them up together
        for i, x in enumerate(arr):
            if i == 0:
                if x % 2 == 0:
                    even[i] = 1
                else:
                    odd[i] = 1
            else:
                if x % 2 == 0:
                    even[i] = even[i - 1] + 1
                    odd[i] = odd[i - 1]
                else:
                    even[i] = odd[i - 1]
                    odd[i] = even[i - 1] + 1

        return sum(odd) % (int(1e9) + 7)
