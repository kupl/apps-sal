class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # worst case is iterate from i -> j -> k and k -> arr.length and test out each comb
        # compute i -> j - 1, keep counter for each i, j comb
        # compute j -> k
        # for each i -> j,
        count = 0
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        for i in range(0, len(arr) - 1):
            for j in range(i + 1, len(arr)):
                target = arr[j - 1]
                if i > 0:
                    target ^= arr[i - 1]
                for k in range(j, len(arr)):
                    curr = arr[k]
                    curr ^= arr[j - 1]
                    if curr == target:
                        count += 1
        return count
