from collections import defaultdict


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_to_chars = defaultdict(list)
        char_int = ord('a')
        for i in range(2, 10):
            num_chars = 3 if i not in {7, 9} else 4
            for j in range(num_chars):
                digit_to_chars[str(i)].append(chr(char_int))
                char_int += 1
        if not digits:
            return []
        letter_combinations = ['']
        for digit in digits:
            new_letter_combinations = []
            for letter_combination in letter_combinations:
                for character in digit_to_chars[digit]:
                    new_letter_combination = letter_combination + character
                    new_letter_combinations.append(new_letter_combination)
            letter_combinations = new_letter_combinations
        return letter_combinations
