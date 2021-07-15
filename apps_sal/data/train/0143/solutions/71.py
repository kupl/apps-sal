class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        prev_count = curr =  count_b = result = 0
        a = None
        b = None
        for c in tree:
            if b == c:
                curr += 1
                count_b += 1
            elif a == c:
                curr += 1
                count_b = 1
                a = b
                b = c
            elif a != c and b != c:
                curr = count_b + 1
                count_b = 1
                a = b
                b = c
            result = max(result, curr)
        return result
