class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        #visited = [False] * len(A)

        visited = collections.Counter(A)

        ans = [0]
        self.calc(A, visited, [], ans)

        return ans[0]

    def calc(self, A, visited, tmp, ans):
        if len(tmp) == len(A):
            ans[0] += 1
            # print(tmp)

        for i in list(visited.keys()):
            if visited[i] == 0:
                continue

            visited[i] -= 1
            tmp.append(i)

            if len(tmp) < 2 or (tmp[-1] + tmp[-2])**(0.5) == int((tmp[-1] + tmp[-2])**(0.5)):
                self.calc(A, visited, tmp, ans)

            tmp.pop()
            visited[i] += 1
