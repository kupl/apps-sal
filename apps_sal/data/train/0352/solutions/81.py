class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        for ele in words:
            ele = list(ele)
        words = sorted(words, key=lambda x: len(x))
        arr = [1] * n
        for i in range(1, n):
            for j in range(0, i):
                if len(words[j]) == len(words[i]) - 1:
                    if(all(x in words[i] for x in words[j])):
                        arr[i] = max(arr[i], arr[j] + 1)
        print(arr)
        return max(arr)
