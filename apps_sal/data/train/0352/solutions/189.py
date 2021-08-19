class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        li = {word: 1 for word in words}
        words.sort(key=len)
        ans = 1
        for word in words:
            for i in range(len(word)):
                new = word[:i] + word[i + 1:]

                if new in words:
                    # print(f\"{new} is in {word}\")
                    # print(f\" {li[word]}  and for new is {li[new] + 1 }\")
                    if li[word] < li[new] + 1:
                       # print(f\" {li[word]}  and for new is {li[new]}\")
                        li[word] = li[new] + 1
                        if li[word] > ans:
                            ans = li[word]
        return ans
