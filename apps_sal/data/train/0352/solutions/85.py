class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordsbylen = collections.defaultdict(list)
        for w in words:
            wordsbylen[len(w)].append(w)

        def get_longest_derivate(word):
            potential = wordsbylen[len(word) + 1]
            possible = [1]
            for p in potential:
                i, j = 0, 0
                while i < len(p) and j < len(word):
                    if p[i] == word[j]:
                        i += 1
                        j += 1
                    elif i != j:
                        break
                    else:
                        i += 1
                if j == len(word):
                    possible.append(1 + get_longest_derivate(p))
            return max(possible)

        return max(map(get_longest_derivate, words))
