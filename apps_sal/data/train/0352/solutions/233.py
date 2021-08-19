class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)

        def extraChar(s1, s2):
            l1, l2 = sorted(s1), sorted(s2)

            diff = 0
            i, j = 0, 0
            if len(s1) == len(s2) + 1:
                while i < len(s1) and j < len(s2):
                    if l1[i] != l2[j]:
                        i += 1
                        diff += 1

                    else:
                        i += 1
                        j += 1

                if i == len(s1) and j == len(s2):
                    return diff == 1
                elif i == len(s1) - 1:
                    return True

            return False

        mem = {}
        words.sort(key=lambda x: len(x))

        def dp(i):
            if i >= n:
                return 0
            if i in mem:
                return mem[i]
            mem[i] = 1
            for j in range(i + 1, n):

                if len(words[j]) == len(words[i]) + 1 and extraChar(words[j], words[i]):
                    #print('words[j]: ', words[j], ' words[j]: ', words[i])
                    mem[i] = max(mem[i], dp(j) + 1)

                elif len(words[j]) > len(words[i]) + 1:
                    break

            return mem[i]

        return max([dp(i) for i in range(n)])
