class Solution:

    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = {}
        for root in dict:
            node = trie
            for letter in root:
                if letter not in node:
                    node[letter] = {}
                node = node[letter]
            node['#'] = root
        words = []
        for word in sentence.split():
            node = trie
            for letter in word:
                if letter not in node or '#' in node:
                    break
                node = node[letter]
            if '#' in node:
                words.append(node['#'])
            else:
                words.append(word)
        return str.join(' ', words)
