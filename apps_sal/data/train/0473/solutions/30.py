class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0
        for j in range(1, n):
            right_xor = collections.defaultdict(int)
            curr_xor = 0
            for k in range(j, n):
                curr_xor ^= arr[k]
                right_xor[curr_xor] += 1
            curr_xor = 0
            for i in range(j - 1, -1, -1):
                curr_xor ^= arr[i]
                if curr_xor in right_xor:
                    count += right_xor[curr_xor]
        return count
