class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        left = 0
        right = len(tokens) - 1
        ans = 0
        curr = 0
        while not left > right:
            if P >= tokens[left]:
                curr += 1
                ans = max(ans, curr)
                P -= tokens[left]
                left += 1
            elif curr > 0:
                P += tokens[right]
                curr -= 1
                right -= 1
            else:
                break

        return ans
