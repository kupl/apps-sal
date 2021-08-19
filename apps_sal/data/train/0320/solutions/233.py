class Solution:
    def minOperations(self, nums) -> int:
        a = list(sorted(nums))

        moves = 0
        while True:
            # make all even
            for i in range(len(a)):
                if a[i] % 2 == 1:
                    moves += 1
                    a[i] -= 1

            # check if done
            remaining = 0
            for i in range(len(a)):
                if a[i] > 0:
                    remaining += 1
            if remaining == 0:
                break

            # divide by 2
            moves += 1
            for i in range(len(a)):
                a[i] = a[i] // 2

        return moves
