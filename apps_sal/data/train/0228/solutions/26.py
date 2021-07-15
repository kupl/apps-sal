class Solution:
    
    # k = substring length. If sliding windows then left & right of sliding window should be different by k
    def maxVowels(self, s: str, k: int) -> int:
        is_a_vowel = lambda letter: letter in 'aeiou'

        count = 0
        maximum_vowels = 0
        
        
        left = 0
        
        for right in range(len(s)):
            # moving right but not touching left pointer
            if right < k:
                count = count + 1 if is_a_vowel(s[right]) else count # add next vowel if present
                maximum_vowels = max(maximum_vowels, count)
            else:
            # moving right and touching left pointer so that distance between pointers is always k
                count = max(0, count-1) if is_a_vowel(s[left]) else count # letter is cut from substrg of k, so decrease count but not lower than 0
                count = count + 1 if is_a_vowel(s[right]) else count # add next vowel if present
                left = left + 1
                maximum_vowels = max(maximum_vowels, count)
        
        return maximum_vowels
        

