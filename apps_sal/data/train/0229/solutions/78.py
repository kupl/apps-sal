class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        cache = collections.Counter(A)
        c_list = sorted(cache, key=lambda x: abs(x))
        print(cache, c_list)
        for x in c_list:
            if cache[x] > cache[2 * x]:
                return False
            cache[2 * x] -= cache[x]
        return True
