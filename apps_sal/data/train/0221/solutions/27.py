class Solution:

    def findRepSubstrGivenLength(self, nums: List[int], l: int, base: int, modulus: int) -> int:
        n = len(nums)
        h = 0
        for i in range(l):
            h = (h * base + nums[i]) % modulus
        seen = {h}
        for start in range(1, n - l + 1):
            h = (h * base - nums[start - 1] * pow(base, l, modulus) + nums[start + l - 1]) % modulus
            if h in seen:
                return start
            seen.add(h)
        return -1

    def longestDupSubstring(self, S: str) -> str:
        if not S:
            return ''
        nums = [ord(S[i]) - ord('a') for i in range(len(S))]
        base = 26
        modulus = 2 ** 32
        left = 1
        right = len(S)
        while left <= right:
            mid = left + (right - left) // 2
            if self.findRepSubstrGivenLength(nums, mid, base, modulus) != -1:
                left = mid + 1
            else:
                right = mid - 1
        start = self.findRepSubstrGivenLength(nums, left - 1, base, modulus)
        return S[start:start + left - 1]


'\nclass Solution:\n    class Node:\n        def __init__(self, v=\'*\'): \n            self.value = v\n            self.next = dict()\n            self.occurences = set()\n                   \n                \n    def print_tree(self, node, indentation):\n        print(indentation + str(node.value) + ": " + str(node.occurences))\n\n        for v in node.next.keys():\n            self.print_tree(node.next[v], indentation + \'\\t\')\n        \n        \n    def getNode(self, node, v):\n        if v not in node.next.keys():\n            node.next[v] = self.Node(v)\n\n        return node.next[v]\n\n\n    def AddOccurences(self, node, i, S):\n        node.occurences.add(i)\n\n        if len(node.occurences) == 2:\n            for o in node.occurences:\n                if o + 1 < len(S):\n                    self.AddOccurences(self.getNode(node, S[o+1]), o+1, S)\n\n\n        if len(node.occurences)>2:\n            if i + 1 < len(S):\n                self.AddOccurences(self.getNode(node, S[i+1]), i+1, S)\n\n        \n    def getLongestDuplicate(self, node):\n        maxSubstring = \'\'\n        \n        for v in node.next.keys():\n            if len(node.next[v].occurences)>1:\n\n                childSubstring = self.getLongestDuplicate(node.next[v])\n                if len(childSubstring) + 1 > len(maxSubstring):\n                    maxSubstring = v + childSubstring\n                        \n        return maxSubstring\n    \n    \n    def longestDupSubstring(self, S: str) -> str:\n        if not S:\n            return 0\n        \n        if len(set(S)) == 1:\n            return S[0:len(S)-1]\n\n        root = self.Node()\n\n        for i in range(len(S)):\n            self.AddOccurences(self.getNode(root, S[i]), i, S)\n\n        #self.print_tree(root, \'\')\n        maxDepthDuplicates = self.getLongestDuplicate(root)\n        \n        return maxDepthDuplicates\n'
