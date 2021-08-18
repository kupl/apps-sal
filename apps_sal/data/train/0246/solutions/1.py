class Solution:

    def replaceWords(self, roots, sentence):

        trie = {}
        for w in roots:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['
        return " ".join([self.replace(i, trie) for i in sentence.split()])

    def replace(self, word, trie):
        cur= trie
        i= 0
        for letter in word:
            if letter not in cur:
                break
            cur= cur[letter]
            i += 1
            if "
                return word[:i]
        return word
