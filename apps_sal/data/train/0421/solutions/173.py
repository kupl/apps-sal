class Node:
    def __init__(self, val=None, is_end=False, children=None):
        self.val = val
        self.children = children if children else {}

class Solution:
    def add_suffix(self, root: Node, s: str):
        for c in s:
            if c not in root.children:
                root.children[c] = Node(val=c)
            root = root.children[c]
        
    def get_last_substring(self, root: Node):
        if not root.children:
            return [root.val]
        return [root.val] + self.get_last_substring(max(root.children.items())[1])
            
    
    def lastSubstring(self, s: str) -> str:
        c = max(s)
        res = ''
        for i,x in enumerate(s):
            if x == c:
                res = max(res, s[i:])
        return res
        # root = Node('')
        # for i in range(len(s)):
        #     self.add_suffix(root, s[i:])
        # return ''.join(self.get_last_substring(root))

