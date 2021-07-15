class Solution:
    def maxArea(self, h: int, w: int, hh: List[int], vv: List[int]) -> int:
        hh = sorted(hh) + [h]
        vv = sorted(vv) + [w]
        prev = 0
        hm = 0
        for i in hh:
            hm = max(hm,i-prev)
            prev = i
        prev = 0
        vm = 0
        for i in vv:
            vm = max(vm,i-prev)
            prev = i
        return (vm * hm)  % (10**9 + 7)
        

