#sort words by length, and we will attempt to shrink longer words and jump backwards to calculated length
#store dictionary of all words, with the chain length being 1
#for each word, iteratively remove one letter (O(k), k = len(word))
#check if the smaller word is now in the dictionary, and if it is, increase the current words chain length to be the smaller words chain + 1
#keep track of longest chain

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_list = sorted(words, key = lambda x: len(x))
        word_dict = {word:1 for word in word_list}
        
        longest = 0
        for word in word_list:
            for i in range(len(word)):
                test = word[:i] + word[i+1:]
                if test in word_dict:
                    word_dict[word] = word_dict[test] + 1
                longest = max(longest, word_dict[word])
        return longest

