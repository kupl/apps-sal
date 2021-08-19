class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indict = defaultdict(list)
        outdict = defaultdict(list)
        for i in range(n):
            if leftChild[i] != -1:
                outdict[i].append(leftChild[i])
                indict[leftChild[i]].append(i)
            if rightChild[i] != -1:
                outdict[i].append(rightChild[i])
                indict[rightChild[i]].append(i)
        rootcount = []
        for nownode in range(n):
            innodelist = indict[nownode]
            if len(innodelist) == 0:
                rootcount.append(nownode)
            if len(innodelist) > 1:
                return False
            for innode in innodelist:
                if innode in outdict[nownode]:
                    return False
        if len(rootcount) != 1:
            return False
        root = rootcount[0]
        ans = []
        visited = {}

        def traverse(node):
            if node == -1:
                return True
            if node in visited:
                return False
            visited[node] = 1
            resleft = traverse(leftChild[node])
            ans.append(node)
            resright = traverse(rightChild[node])
            if resleft == False or resright == False:
                return False
            return True
        res = traverse(root)
        if len(ans) == n and res == True:
            return True
        return False
