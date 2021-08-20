class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        possibilities = set()

        def swap(arr, l, r):
            if l == r:
                return
            (arr[l], arr[r]) = (arr[r], arr[l])

        def add_permutation(arr):
            nonlocal possibilities
            for i in range(len(arr)):
                possibilities.add(''.join(arr[:i + 1]))

        def build_permutations(arr, start=0):
            if start >= len(arr):
                add_permutation(arr)
                return
            for i in range(start, len(arr)):
                swap(arr, i, start)
                build_permutations(arr, start + 1)
                swap(arr, i, start)
        build_permutations(list(tiles))
        return len(possibilities)
