class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def getAtMost(K):
            freq = defaultdict(int)

            subarray_count = 0
            left = 0

            for right, num in enumerate(A):
                freq[num] += 1

                while len(freq) > K:
                    freq[A[left]] -= 1

                    if freq[A[left]] == 0:
                        del freq[A[left]]

                    left += 1

                subarray_count += right - left + 1

            return subarray_count

        return getAtMost(K) - getAtMost(K - 1)
