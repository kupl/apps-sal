class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words.sort(key=lambda w: len(w))

        def predecessor(a: str, b: str):
            if len(b) - len(a) == 1:
                mismatch = 0
                a_idx, b_idx = 0, 0

                while a_idx < len(a) and mismatch <= 1:

                    if a[a_idx] != b[b_idx]:
                        mismatch += 1
                        b_idx += 1
                    else:
                        a_idx = a_idx + 1
                        b_idx = b_idx + 1

                if mismatch == 1 or not mismatch:
                    return True

            return False

        dp = [1]
        for word in words[1:]:
            max_length = 1
            for i in range(len(dp)):
                if predecessor(words[i], word):
                    max_length = max(max_length, dp[i] + 1)

            dp.append(max_length)

        return max(dp)
