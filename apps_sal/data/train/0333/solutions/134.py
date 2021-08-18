class Solution:
    def minJumps(self, arr: List[int]) -> int:
        from collections import defaultdict, deque
        n = len(arr)

        indices = defaultdict(list)

        for i in range(n):
            indices[arr[i]].append(i)

        visited = [False] * n
        visited[0] = True

        queue = deque()
        queue.append(0)

        steps = 0

        while len(queue) > 0:
            for size in range(len(queue), 0, -1):
                i = queue.popleft()

                if i == n - 1:
                    return steps

                next = indices[arr[i]]

                next.append(i - 1)
                next.append(i + 1)

                for num in next:
                    if num >= 0 and num < n and not visited[num]:
                        visited[num] = True
                        queue.append(num)

                indices[arr[i]] = []

            steps += 1

        return 0
