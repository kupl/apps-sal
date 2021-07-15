import numpy as np
class Solution:
    def longestCommonSubsequence(self, answer_text: str, source_text: str) -> int:
        longest = 0
        answer_text = ' ' + answer_text
        source_text = ' ' + source_text
        words_matrix = np.zeros((len(source_text), len(answer_text)))
        for row in range(1, len(source_text)):
            for col in range(1, len(answer_text)):
                if source_text[row] == answer_text[col]:
                    words_matrix[row][col] = words_matrix[row - 1][col - 1] + 1
                else:
                    words_matrix[row][col] = max(words_matrix[row - 1][col], words_matrix[row][col - 1])
                longest = max(longest, words_matrix[row][col])
        return int(longest)
