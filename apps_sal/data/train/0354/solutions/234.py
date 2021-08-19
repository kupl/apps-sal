class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        @lru_cache(maxsize=None)
        # @func DFS: depth-first search on the chance of rolling a given combination
        # @param n: the number of chances you have left to roll
        # @param i: the number you roll
        # @param k: counter for the number of times this number was repeated
        def DFS(n, i, k):
            # If there is no more chances left (this is a combination)..
            if not n:
                # Count the combintation as a single one
                return 1

            # Create a counter to determine the number of possible combintations with this configuration
            numSequences = 0

            # For each roll of the die
            for j in range(6):
                # If this element is not the one currently rolled..
                if not i == j:
                    # Add the combination sequences, of this given i, then j sequence
                    numSequences += DFS(n - 1, j, 1)

                # If adding another roll of this element is possible given the constraints..
                elif k + 1 <= rollMax[j]:
                    # Add the combintation sequence, of this given i, then i (technically j)
                    numSequences += DFS(n - 1, j, k + 1)

            return numSequences

        return sum(DFS(n - 1, i, 1) for i in range(6)) % 1000000007
