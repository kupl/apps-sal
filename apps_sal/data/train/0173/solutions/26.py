class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        if sum(arr) % k != 0:
            return False
        mod = defaultdict(int)
        for num in arr:
            if k - num % k in mod and mod[k - num % k] != 0:
                mod[k - num % k] -= 1
            else:
                mod[num % k] += 1
        print(mod)
        for (k, v) in mod.items():
            if k * v != 0:
                return False
        return True
