class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        children = set()
        children.add(0)
        for i in range(n):
            l = [leftChild[i], rightChild[i]]

            for c in l:
                if c != -1:
                    if i in children:
                        if c in children:
                            return False
                        else:
                            children.add(c)
                    else:
                        if c in children:
                            children.add(i)
                        else:
                            return False

        return len(children) == n
