class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        if len(words) == 0:
            return 0

        def isRelate(small: str, big: str) -> bool:
            for i in range(len(big)):
                if small == big[:i] + big[i + 1:]:
                    return True
            return False

        def lengthList(target: int) -> List[str]:
            if target == 0:
                return []
            final = []
            for i in words:
                if len(i) == target:
                    final.append(i)
            return final

        dp = collections.defaultdict(int)
        words.sort(key=lambda x: len(x))
        for word in words:
            compareList = lengthList(len(word) - 1)
            maxx = 0
            if len(compareList) == 0:
                dp[word] = 1
            else:

                for small in compareList:
                    if isRelate(small, word):
                        maxx = max(maxx, dp[small])

                dp[word] = maxx + 1

        return max(dp.values())


#         def recur(word:str,words:List[str],remain:List[str],length:int):
#             if len(word)==len(max(words)) and len(remain)==0:
#                 return 1
