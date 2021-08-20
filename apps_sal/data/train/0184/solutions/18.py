class Solution:

    def maxRepOpt1(self, text: str) -> int:

        def get_possible(idx, cur, step, swap):
            if idx >= len(positions):
                return step + swap
            if positions[idx] - 1 == cur:
                return get_possible(idx + 1, positions[idx], step + 1, swap)
            elif not swap:
                return step
            else:
                return max(step + 1, get_possible(idx, cur + 1, step + 1, False), get_possible(idx, positions[idx] - 1, 1, False), get_possible(idx + 1, positions[idx], 1, True))
        (letters, ans) = (defaultdict(list), 0)
        for (i, c) in enumerate(text):
            letters[c].append(i)
        for (_, positions) in letters.items():
            if len(positions) < 3:
                ans = max(ans, len(positions))
                continue
            x = min(get_possible(1, positions[0], 1, True), len(positions))
            ans = max(x, ans)
        return ans
