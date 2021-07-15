class Solution:
    def countVowelPermutation(self, n: int) -> int:

        graph = {
            0: (1,),
            1: (0, 2),
            2: (0, 1, 3, 4),
            3: (2, 4),
            4: (0,),
        }

        permutations = [1] * 5
        for _ in range(n - 1):
            next_permutations = [0] * 5
            for node in range(5):
                for neighbour in graph[node]:
                    next_permutations[neighbour] += permutations[node]
            permutations = next_permutations

        return sum(permutations) % (10 ** 9 + 7)
