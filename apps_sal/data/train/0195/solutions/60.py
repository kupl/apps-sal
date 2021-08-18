class TrieNode:
    def __init__(self):
        self.children = [None] * 2
        self.count = 0
        self.cache = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        now = self.root
        for j in range(16):
            i = num & 1
            if not now.children[i]:
                now.children[i] = TrieNode()
            now = now.children[i]
            num >>= 1
        now.count += 1

    def match(self, num):
        return self.count_match(self.root, num)

    def count_match(self, now, num):
        if not now:
            return 0

        if num in now.cache:
            return now.cache[num]

        if now.count > 0:
            return now.count

        bit = num & 1
        next_num = num >> 1
        if bit:
            now.cache[num] = self.count_match(now.children[0], next_num)

        else:
            tmp = 0
            tmp += self.count_match(now.children[0], next_num)
            tmp += self.count_match(now.children[1], next_num)
            now.cache[num] = tmp

        return now.cache[num]


class Solution:
    def countTriplets(self, A: List[int]) -> int:

        trie = Trie()

        for num in A:
            trie.insert(num)

        cache = {}
        ans = 0
        for num1 in A:
            for num2 in A:
                num = (num1 & num2)
                a = trie.match(num)
                ans += a
        return ans
