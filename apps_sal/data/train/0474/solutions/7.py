from collections import Counter


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letters_dict = Counter(letters)
        res = []
        max_score = 0
        size = len(words)

        def subsets(start, curr):
            res.append(curr)
            for i in range(start, len(words)):
                subsets(i + 1, curr + [words[i]])
        subsets(0, [])
        flag = 0
        for subset in res:
            curr_score = 0
            curr_letters_dict = dict(letters_dict)
            for word in subset:
                for char in word:
                    if char in curr_letters_dict and curr_letters_dict[char] > 0:
                        curr_score += score[ord(char) - ord('a')]
                        curr_letters_dict[char] -= 1
                    else:
                        flag = 1
                        break
                if flag:
                    break
            if flag:
                flag = 0
            else:
                max_score = max(max_score, curr_score)
        return max_score
