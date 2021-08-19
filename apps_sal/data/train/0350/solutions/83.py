class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        def longest_with_atmostk(s, k):
            start = 0
            counts = defaultdict(int)  # keep count of each character
            n_chars = 0  # store the length of the string from start to current index
            max_len = 0  # maximum possible length
            for i in range(len(s)):
                if counts[s[i]] == 0:  # if the character is never seen before increase length of the current string

                    n_chars += 1
                counts[s[i]] += 1  # increase the count of the current character
                while n_chars > k:  # if there is no repeating characters the length of the string should be i-start+1
                    if counts[s[start]] > 0:  # if the start
                        counts[s[start]] -= 1
                        if counts[s[start]] == 0:
                            n_chars -= 1
                    start += 1
                max_len += i - start + 1

            return max_len

        return longest_with_atmostk(A, K) - longest_with_atmostk(A, K - 1)
