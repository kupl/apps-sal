class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        (run, prev) = ([], 0)
        count = 0
        (odd, even) = (0, 0)
        for ele in arr:
            run.append(prev + ele)
            prev = run[-1]
            if run[-1] % 2 != 0:
                count += even + 1
                odd += 1
            else:
                count += odd
                even += 1
        return count % (10 ** 9 + 7)
