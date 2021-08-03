class Solution:
    def numTeams(self, rating: List[int]) -> int:
        self.ans = 0

        def traverse(idx, arr, direction):
            if len(arr) == 3:
                self.ans += 1
                return
            for j in range(idx, len(rating) - (2 - len(arr))):

                if direction == 'up' and rating[j] > arr[-1]:
                    traverse(j + 1, arr.copy() + [rating[j]], direction)
                if direction == 'down' and rating[j] < arr[-1]:
                    traverse(j + 1, arr.copy() + [rating[j]], direction)

        for i in range(0, len(rating) - 2):
            traverse(i + 1, [rating[i]], 'up')
            traverse(i + 1, [rating[i]], 'down')

        return self.ans
