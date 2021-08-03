from collections import defaultdict


class TrieNode:
    def __init__(self, x=None):
        self.val = x
        self.end = False
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.max_len = 0

    def insert(self, word):
        node = self.root
        for i, w in enumerate(word):
            node.children[w].val = w
            node = node.children[w]
            self.root.children[w] = node
            if i == len(w) - 1:
                node.end = True

    def find(self, word):
        node = self.root
        d = 0
        for w in word[:-1]:
            print(w, node.children.keys())
            node = node.children[w]
            d += 1
            if node.end:
                print(node.val, node.end)
                self.max_len = max(self.max_len, d)


class Solution:
    def longestPrefix(self, s):
        res, l, r, mod = 0, 0, 0, 10**9 + 7
        for i in range(len(s) - 1):
            l = (l * 128 + ord(s[i])) % mod
            r = (r + pow(128, i, mod) * ord(s[~i])) % mod
            if l == r:
                res = i + 1
        return s[:res]
