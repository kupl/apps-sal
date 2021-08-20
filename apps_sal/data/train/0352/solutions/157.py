class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        predecessors = dict()
        words = sorted(words, key=len)
        for i in range(len(words)):
            predecessors[words[i]] = []
            for j in range(i):
                if self.isPredecessor(words[i], words[j]):
                    predecessors[words[i]].append((words[j], j))
        print(words)
        print(predecessors)
        T = [0] * len(words)
        T[0] = 1
        for i in range(1, len(words)):
            if predecessors[words[i]]:
                T[i] = max([T[j[1]] for j in predecessors[words[i]]]) + 1
            else:
                T[i] = 1
        return max(T)

    def isPredecessor(self, word, candidate):
        if len(candidate) + 1 != len(word):
            return False
        (i, j) = (0, 0)
        wildcard = True
        while i < len(word) and j < len(candidate):
            if word[i] == candidate[j]:
                i += 1
                j += 1
            elif wildcard:
                i += 1
                wildcard = False
            else:
                return False
        return i + 1 == len(word) or i == len(word) if wildcard else i == len(word)
