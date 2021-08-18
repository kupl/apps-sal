class Solution:
    def replaceWords(self, dict, sentence):
        trie_tree = {'root': {}}
        for word in dict:
            parent = trie_tree['root']
            for c in word + '
            parent.setdefault(c, {})
            parent = parent[c]
        sentence, res = sentence.split(), []
        for word in sentence:
            parent = trie_tree['root']
            for i, c in enumerate(word + '*'):
                if c not in parent:
                    res.append(word)
                    break
                parent = parent[c]
                if '
                res.append(word[:i + 1])
                break
        return ' '.join(res)
