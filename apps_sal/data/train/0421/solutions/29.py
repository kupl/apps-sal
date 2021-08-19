class Solution:
    # build the suffix tree of the string and traverse the tree by always pick the right most branch.
    def lastSubstring(self, s: str) -> str:
        class TreeNode:
            def __init__(self):
                self.children = collections.defaultdict()

        # build the suffix tree
        root = TreeNode()
        for start in range(len(s)):
            node = root
            for c in s[start:]:
                if c not in node.children:
                    node.children[c] = TreeNode()
                node = node.children[c]
        # traverse the tree
        res = ''
        node = root
        while node and len(node.children) > 0:
            for i in range(25, -1, -1):  # find the rightmost available branch
                c = chr(ord('a') + i)
                if c in node.children:
                    node = node.children[c]
                    res += c
                    break
        return res

    # It can be seen that the last substring in lexicographical order is always a suffix of the string.
    # Start with all possible suffix strings. Each time eliminate the ones not started from the largest letter.
    # Continue until there is only one distinct letter.
    def lastSubstring(self, s: str) -> str:
        i, indexes = 0, list(range(len(s)))
        while len(indexes) > 1:
            new = []
            mx = max([s[i + j] for j in indexes if i + j < len(s)])
            for k, j in enumerate(indexes):
                if k - 1 >= 0 and indexes[k - 1] + i == j:
                    continue
                if i + j >= len(s):
                    break
                if s[i + j] == mx:
                    new.append(j)
            i += 1
            indexes = new
        return s[indexes[0]:]
