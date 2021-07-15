class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        ans, dicti, memo = 0, collections.defaultdict(list), collections.defaultdict(int)
        for word in words:
            dicti[len(word)].append(word)
        chars = [chr(ch) for ch in range(ord('a'), ord('z')+1)]
        
        def find(count, word):
            if word in memo:
                return count + memo[word]
            if len(word) + 1 not in dicti:
                memo[word] = 0
                return count
                
            maxi = 0
            for i in range(len(word)+1):
                for ch in chars:
                    new_word = word[:i] + ch + word[i:]
                    if new_word in dicti[len(word)+1]:
                        maxi = max(maxi, find(1, new_word))
            memo[word] = maxi
            return count + memo[word]
        
        for word in sorted(words, key=lambda x:len(x)):
            el = find(1, word)
            # print(el, word)
            ans = max(ans, el)
        return ans

            

