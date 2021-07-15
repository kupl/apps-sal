from collections import defaultdict
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        def search(i: int, j: int, carry: int, used: int, ls: list, mp: defaultdict, non_zeros: set) -> bool:
            if j == len(ls[-1]):
                return carry == 0
            if i == len(ls):
                total = sum([mp[ls[r][j]] if j < len(ls[r]) else 0 for r in range(len(ls) - 1)]) + carry
                exp_total = mp[ls[-1][j]]
                if (total % 10) != exp_total:
                    return False
                return search(0, j + 1, total // 10, used, ls, mp, non_zeros)
            if j >= len(ls[i]) or ls[i][j] in mp:
                return search(i + 1, j, carry, used, ls, mp, non_zeros)
            start = 1 if ls[i][j] in non_zeros else 0
            for d in range(start, 10):
                if (1 << d) & used:
                    continue
                mp[ls[i][j]] = d
                if search(i + 1, j, carry, used | (1 << d), ls, mp, non_zeros):
                    mp.pop(ls[i][j])
                    return True
                mp.pop(ls[i][j])
            return False
        
        non_zeros = set([w[0] for w in words] + [result[0]])
        ls = [w[::-1] for w in words] + [result[::-1]]
        return search(0, 0, 0, 0, ls, defaultdict(int), non_zeros)
