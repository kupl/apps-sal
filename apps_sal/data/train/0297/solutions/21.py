class Solution:

    def numTilePossibilities(self, tiles: str) -> int:

        def dfs(state):
            res.append(state.copy())
            for i in range(len(state)):
                if state[i] < full_state[i]:
                    state[i] += 1
                    dfs(state)
                    state[i] -= 1
        memo = collections.Counter(tiles)
        full_state = list(memo.values())
        state = [0 for _ in range(len(memo))]
        res = []
        dfs(state)
        return len(res) - 1
