class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        res_map = {}
        for idx in range(len(fronts)) :
            if fronts[idx] == backs[idx] :
                res_map.setdefault(fronts[idx], False)
                res_map[fronts[idx]] = False
            else :
                res_map.setdefault(fronts[idx], True)
                res_map.setdefault(backs[idx], True)
        for num in sorted(res_map.keys()) :
            if res_map[num] : return num
        return 0
