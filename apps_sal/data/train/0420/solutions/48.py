class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        # Make a dict of vowels and sequental orders of 2**n 
        # the values are used as bit masks 
        vowels_bit_mask = {v:2**i for i, v in enumerate('aeiou')}
        vowel_state = 0
        first_index_of_recorded_state = {0:-1}
        max_substr_len = 0
        for index, char in enumerate(s):
            if char in vowels_bit_mask:
                # bitwise xor of the current state of the vowels 
                # with the inclusion of the new vowel
                # i.e A +  E = A+E
                # 0100 ^= 0001 = 0101
                vowel_state ^= vowels_bit_mask[char]
                
            if vowel_state in first_index_of_recorded_state:
                max_substr_len = max(max_substr_len, index-first_index_of_recorded_state[vowel_state])
            else:
                first_index_of_recorded_state[vowel_state] = index
        return max_substr_len
            
            
            
            
            
            
        
                

