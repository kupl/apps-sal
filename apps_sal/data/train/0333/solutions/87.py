class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # return self.bfs(arr)
        return self.minJumpsBiBFS(arr)

    def bfs(self, arr: List[int]):
        arrLen = len(arr)
        if arrLen <= 1:
            return 0
        adjList = defaultdict(set)
        for i in range(len(arr)):
            adjList[arr[i]].add(i)
        queue = deque([0])
        visited = set([0])
        jump = 0

        while queue:
            length = len(queue)

            for _ in range(length):
                node = queue.popleft()
                for nei in adjList[arr[node]]:
                    if nei == arrLen - 1:
                        return jump + 1
                    if nei in visited:
                        continue
                    visited.add(nei)
                    queue.append(nei)
                adjList[arr[node]].clear()

                if node + 1 < arrLen:
                    if node + 1 == arrLen - 1:
                        return jump + 1
                    if node + 1 not in visited:
                        visited.add(node + 1)
                        queue.append(node + 1)

                if node - 1 >= 0:
                    if node - 1 == arrLen - 1:
                        return jump + 1
                    if node - 1 not in visited:
                        visited.add(node - 1)
                        queue.append(node - 1)
            jump += 1
        return -1

    def minJumpsBiBFS(self, arr: List[int]) -> int:
        arrLen = len(arr)
        if arrLen <= 1:
            return 0
        adjList = defaultdict(set)
        for i in range(len(arr)):
            adjList[arr[i]].add(i)
        frontQueue = deque([0])
        rearQueue = deque([len(arr) - 1])
        visited = set([0])
        jump = 0

        while frontQueue or rearQueue:
            if len(frontQueue) > len(rearQueue):
                frontQueue, rearQueue = rearQueue, frontQueue
            length = len(frontQueue)

            for _ in range(length):
                node = frontQueue.popleft()
                for nei in adjList[arr[node]]:
                    if nei in rearQueue:
                        return jump + 1
                    if nei in visited:
                        continue
                    visited.add(nei)
                    frontQueue.append(nei)
                adjList[arr[node]].clear()

                if node + 1 < arrLen:
                    if node + 1 in rearQueue:
                        return jump + 1
                    if node + 1 not in visited:
                        visited.add(node + 1)
                        frontQueue.append(node + 1)

                if node - 1 >= 0:
                    if node - 1 in rearQueue:
                        return jump + 1
                    if node - 1 not in visited:
                        visited.add(node - 1)
                        frontQueue.append(node - 1)
            jump += 1
        return -1
