class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        print(len(piles) % 3)
        piles = sorted(piles)
        print(piles)
        score = 0
        if len(piles) % 3 == 0:
            tmp = piles[int(len(piles) / 3):]
            nums = [tmp[i] for i in range(0, len(tmp), 2)]
            print(sum(nums))
            return sum(nums)
        elif len(piles) % 3 == 2:
            tmp = piles[int(len(piles) / 3):]
            nums = [tmp[i] for i in range(0, len(tmp), 2)]
            print(sum(nums))
            return sum(nums)
        else:
            tmp = piles[int(len(piles) / 3):]
            nums = [tmp[i] for i in range(1, len(tmp), 2)]
            print(sum(nums))
            return sum(nums)
