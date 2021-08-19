class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        #  directed graph
        # each node except root has exactly 1 indegree
        # each node can have only 0~2 children

        graph = collections.defaultdict(list)
        indegree = {nodeNum: 0 for nodeNum in range(n)}

        for nodeNum in range(n):
            left = leftChild[nodeNum]
            right = rightChild[nodeNum]

            graph[nodeNum] = []
            if left != -1:
                graph[nodeNum].append(left)
                indegree[left] += 1
            if right != -1:
                graph[nodeNum].append(right)
                indegree[right] += 1

        # print(indegree)
        zeroIndegrees = collections.deque([])
        singleIndegrees = 0

        for nodeNum, indegrees in list(indegree.items()):
            if indegrees == 0:
                zeroIndegrees.append(nodeNum)
            elif indegrees == 1:
                singleIndegrees += 1
            else:
                return False

        if len(zeroIndegrees) != 1:
            return False

        if len(zeroIndegrees) + singleIndegrees != n:
            return False

        print(zeroIndegrees)
        topological_sort = []
        while zeroIndegrees:
            nodeNum = zeroIndegrees.popleft()
            topological_sort.append(nodeNum)

            if nodeNum in graph:
                for child in graph[nodeNum]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        zeroIndegrees.append(child)

        if len(topological_sort) == n:
            return True
        return False

# 4
# [1,0,3,-1]
# [-1,-1,-1,-1]

# 0               2
#     1         3
