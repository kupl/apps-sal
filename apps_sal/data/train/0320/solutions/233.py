class Solution:

    def minOperations(self, nums) -> int:
        a = list(sorted(nums))
        moves = 0
        while True:
            for i in range(len(a)):
                if a[i] % 2 == 1:
                    moves += 1
                    a[i] -= 1
            remaining = 0
            for i in range(len(a)):
                if a[i] > 0:
                    remaining += 1
            if remaining == 0:
                break
            moves += 1
            for i in range(len(a)):
                a[i] = a[i] // 2
        return moves
