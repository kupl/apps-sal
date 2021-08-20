from copy import deepcopy


class Solution:

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        queue = [[letters, 0, words]]
        visited = []
        max = 0
        while len(queue) != 0:
            item = queue.pop(0)
            if item[0] in visited:
                continue
            visited.append(item[0])
            for word in item[2]:
                lettersCopy = deepcopy(item[0])
                hasEnoughChars = self.hasEnoughChars(lettersCopy, word, score)
                if hasEnoughChars != -1 and lettersCopy not in visited:
                    if item[1] + hasEnoughChars > max:
                        max = item[1] + hasEnoughChars
                    wordsCopy = deepcopy(item[2])
                    wordsCopy.remove(word)
                    queue.append([lettersCopy, item[1] + hasEnoughChars, wordsCopy])
        return max

    def charValue(self, letter: str):
        return ord(letter) - 97

    def hasEnoughChars(self, letters, word, score):
        sum = 0
        try:
            for x in list(word):
                letters.remove(x)
                sum += score[self.charValue(x)]
        except:
            return -1
        return sum
