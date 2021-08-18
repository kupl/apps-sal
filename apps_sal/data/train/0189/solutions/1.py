class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:

        preference_list = [[0 for _ in range(n)] for _ in range(n)]

        for x in range(n):
            for i, y in enumerate(preferences[x]):
                preference_list[x][y] = n - i - 1

        unhappy = {}
        for i in range(n // 2):
            x, y = pairs[i]
            for j in range(n // 2):
                u, v = pairs[j]
                if i != j:
                    if ((preference_list[x][y] < preference_list[x][u] and preference_list[u][x] > preference_list[u][v]) or (preference_list[x][y] < preference_list[x][v] and preference_list[v][u] < preference_list[v][x])):
                        unhappy[x] = 1
                    if ((preference_list[y][x] < preference_list[y][u] and preference_list[u][y] > preference_list[u][v]) or (preference_list[y][x] < preference_list[y][v] and preference_list[v][u] < preference_list[v][y])):
                        unhappy[y] = 1
        res = len(unhappy)

        return res
