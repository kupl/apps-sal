class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        best_ans = 1
        cur_ans = set()

        def find_result(i):
            nonlocal best_ans
            if i >= len(s):
                return len(cur_ans)
            elif len(s) - i + len(cur_ans) < best_ans:
                return best_ans

            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if substr not in cur_ans:
                    cur_ans.add(substr)
                    best_ans = max(best_ans, find_result(j))
                    cur_ans.remove(substr)

            return max(best_ans, len(cur_ans))

        return find_result(0)
