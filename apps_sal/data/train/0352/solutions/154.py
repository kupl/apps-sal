class Solution:

    def can_move(self, a, b):
        b_letters = Counter(b)

        for char in a:
            b_letters[char] -= 1

            if b_letters[char] < 0:
                return False
            elif b_letters[char] == 0:
                b_letters.pop(char)

        return b_letters.popitem()[1] == 1

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda w: len(w))

        depths = {}

        def recur(index):
            if index not in depths:
                s = words[index]

                mx = 0
                for i in range(index + 1, len(words)):
                    if len(words[i]) - len(s) == 1 and self.can_move(s, words[i]):
                        mx = max(recur(i), mx)

                depths[index] = mx + 1

            return depths[index]

        for i in range(len(words)):
            recur(i)

        return max(depths.values())
