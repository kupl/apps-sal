class Solution:
    def numSplits(self, s: str) -> int:
        # preprocess_prefix[k], number of different letters in s[:k]
        # preprocess_postfix[k], number of different letters in s[k:]
        
        # Fill preprocess_prefix
        seen_letters = []
        preprocess_prefix = [0]
        for i in range(len(s)):
            if s[i] not in seen_letters:
                seen_letters.append(s[i])
            preprocess_prefix.append(len(seen_letters))
        
        # Fill preprocess_postfix[k]
        seen_letters = []
        preprocess_postfix = [0]
        for i in range(len(s)-1, -1, -1):
            if s[i] not in seen_letters:
                seen_letters.append(s[i])
            preprocess_postfix.append(len(seen_letters))
        preprocess_postfix.reverse()
        count = 0
        for i in range(len(preprocess_postfix)):
            if preprocess_postfix[i] == preprocess_prefix[i]:
                count += 1
        return count
