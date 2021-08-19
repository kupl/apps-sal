class Solution:

    def lastSubstring(self, s: str) -> str:

        class TreeNode:

            def __init__(self):
                self.children = collections.defaultdict()
        root = TreeNode()
        for start in range(len(s)):
            node = root
            for c in s[start:]:
                if c not in node.children:
                    node.children[c] = TreeNode()
                node = node.children[c]
        res = ''
        node = root
        while node and len(node.children) > 0:
            for i in range(25, -1, -1):
                c = chr(ord('a') + i)
                if c in node.children:
                    node = node.children[c]
                    res += c
                    break
        return res

    def lastSubstring(self, s: str) -> str:
        (i, indexes) = (0, list(range(len(s))))
        while len(indexes) > 1:
            new = []
            mx = max([s[i + j] for j in indexes if i + j < len(s)])
            for (k, j) in enumerate(indexes):
                if k - 1 >= 0 and indexes[k - 1] + i == j:
                    continue
                if i + j >= len(s):
                    break
                if s[i + j] == mx:
                    new.append(j)
            i += 1
            indexes = new
        return s[indexes[0]:]
