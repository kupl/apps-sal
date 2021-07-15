class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def solve(start, visited, memo):
            state = (start, tuple(visited))
            if start >= len(s):
                return 0
            if state in memo:
                return memo[state]
            result = 0
            for idx in range(start, len(s)):
                cut_str = s[start:idx + 1]
                pos = get_position(cut_str)
                if visited[pos]:
                    continue
                visited[pos] = True
                
                result = max(result, 1 + solve(idx + 1, visited, memo))
                visited[pos] = False
            memo[state] = result
            return result
        def get_position(string):
            return self.sub_str_pos[string]
        self.sub_str_pos = {}
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub_str = s[i:j + 1]
                if sub_str not in self.sub_str_pos:
                    self.sub_str_pos[sub_str] = len(self.sub_str_pos)
        return solve(0, [False for _ in range(len(self.sub_str_pos))], {})

