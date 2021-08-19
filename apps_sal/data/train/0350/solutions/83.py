class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        def longest_with_atmostk(s, k):
            start = 0
            counts = defaultdict(int)
            n_chars = 0
            max_len = 0
            for i in range(len(s)):
                if counts[s[i]] == 0:
                    n_chars += 1
                counts[s[i]] += 1
                while n_chars > k:
                    if counts[s[start]] > 0:
                        counts[s[start]] -= 1
                        if counts[s[start]] == 0:
                            n_chars -= 1
                    start += 1
                max_len += i - start + 1
            return max_len
        return longest_with_atmostk(A, K) - longest_with_atmostk(A, K - 1)
