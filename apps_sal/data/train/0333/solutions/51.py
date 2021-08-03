class Solution:
    def minJumps(self, arr: List[int]) -> int:
        dic = defaultdict(list)
        for i in range(len(arr)):
            dic[arr[i]].append(i)
        visited = [False] * (len(arr))
        queue = collections.deque()
        queue.append((0, 0))
        ans = 0
        N = len(arr)
        while(queue):
            i, step = queue.popleft()
            print((i, step))
            if(i == N - 1):
                ans = step
                break
            if visited[i] == False:
                if(i + 1 < N):
                    queue.append((i + 1, step + 1))
                if(i - 1 >= 0):
                    queue.append((i - 1, step + 1))
                for index in dic[arr[i]]:
                    if(visited[index] == False):
                        queue.append((index, step + 1))
                visited[i] = True
                dic[arr[i]] = []

        return ans
