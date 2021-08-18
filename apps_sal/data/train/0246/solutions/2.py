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
            node["

        words = []
        for word in sentence.split():
            node = trie
            for letter in word:
                if letter not in node or "
                    break
                node = node[letter]
            if "
                words.append(node["
            else:
                words.append(word)
        return str.join(" ", words)
