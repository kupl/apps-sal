class Solution:
    def numTeams(self, rating: List[int]) -> int:

        target = 3
        self.count = 0
        self.lst = []

        def isSolution(candidate_count):
            if candidate_count == target:
                return True

        def isViable(rating, i, candidates, candidate_count, direction):
            if i == 0 or candidate_count == 0:
                return True

            if direction == -1 and rating[i] < candidates[-1]:
                return True
            if direction == 1 and rating[i] > candidates[-1]:
                return True
            return False

        def backtrack(index, rating, candidates, candidate_count, direction):
            if isSolution(candidate_count):
                self.count += 1
                return

            for i in range(index, len(rating)):
                if isViable(rating, i, candidates, candidate_count, direction):
                    candidates.append(rating[i])
                    backtrack(i + 1, rating, candidates, candidate_count + 1, direction)
                    candidates.pop()

        directions = [1, -1]
        for direction in directions:
            backtrack(0, rating, [], 0, direction)
        return self.count
