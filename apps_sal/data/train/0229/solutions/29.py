class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        dicti = dict()
        for var in arr:
            if var in list(dicti.keys()):
                dicti[var] += 1
            else:
                dicti[var] = 1
        arr.sort(key=lambda x: abs(x))
        for var in arr:
            if dicti[var] == 0:
                continue
            if(2 * var not in list(dicti.keys())):
                return False
            if dicti[2 * var] <= 0:
                return False
            dicti[var] -= 1
            dicti[2 * var] -= 1
        return True
