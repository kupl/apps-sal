class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        (bitmask_to_index, bitmaskrepr, result) = ({0: -1}, 0, 0)
        for (index, item) in enumerate(s):
            if item in vowels:
                bitmaskrepr ^= vowels[item]
            if bitmaskrepr not in bitmask_to_index:
                bitmask_to_index[bitmaskrepr] = index
            else:
                result = max(result, index - bitmask_to_index[bitmaskrepr])
        return result
