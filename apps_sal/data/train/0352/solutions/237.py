class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        hashmap = collections.defaultdict(list)
        for index, word in enumerate(words):
            hashmap[len(word)].append(index)
        n = len(words)
        graph = [[False for _ in range(n)] for _ in range(n)]

        def predecessor(a, b):
            mistake = 0
            for i in range(len(a)):
                if a[i] != b[i + mistake]:
                    mistake += 1
                    if mistake > 1 or a[i] != b[i + mistake]:
                        return False
            return True

        for index, word in enumerate(words):
            for candidate in hashmap[len(word) + 1]:
                if predecessor(word, words[candidate]):
                    graph[index][candidate] = True
        dp = [-1 for _ in range(n)]

        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            answer = 0
            for j in range(n):
                if graph[i][j]:
                    answer = max(answer, dfs(j))
            dp[i] = answer + 1
            #print(f'i = {i}, dp[i]={dp[i]}')
            return answer + 1

        answer = 0
        for i in range(n):
            answer = max(answer, dfs(i))
        return answer
