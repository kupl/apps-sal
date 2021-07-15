class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        best_attempt = 0
        for i in range(len(tree)):
            baskets = {}
            for j in range(i, len(tree)):
                if tree[j] in baskets:
                    baskets[tree[j]] += 1
                elif len(baskets) >= 2:
                    break
                else:
                    baskets[tree[j]] = 1
            attempt_val = sum(baskets.values())
            if attempt_val > best_attempt:
                best_attempt = attempt_val
            if best_attempt > len(tree) - i:
                break
        return best_attempt
        

