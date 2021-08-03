class Solution:
    def allPrefixXor(self, arr: List[int]) -> List[int]:
        prefix_xor: List[int] = [0] * len(arr)

        prefix_xor[0] = arr[0]
        for i in range(1, len(arr)):
            prefix_xor[i] = prefix_xor[i - 1] ^ arr[i]

        return prefix_xor

    def allSegmentXor(self, arr: List[int]) -> List[List[int]]:
        prefix_xor: List[int] = self.allPrefixXor(arr)
        segment_xor: List[List[int]] = [[0] * len(arr) for _ in range(len(arr))]

        segment_xor[0] = prefix_xor[:]
        for first in range(1, len(segment_xor) - 1):
            for last in range(first + 1, len(segment_xor[first])):
                segment_xor[first][last] = prefix_xor[last] ^ prefix_xor[first - 1]

        return segment_xor

    def countTriplets(self, arr: List[int]) -> int:
        segment_xor: List[List[int]] = self.allSegmentXor(arr)
        n_triplets: int = 0

        for first in range(len(segment_xor) - 1):
            for last in range(first + 1, len(segment_xor[first])):
                if segment_xor[first][last] == 0:
                    n_triplets += last - first

        return n_triplets
