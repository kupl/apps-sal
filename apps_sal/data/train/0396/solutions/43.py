class Solution:

    def smallestRepunitDivByK(self, K: int) -> int:
        seen_mod = set()
        current = 1
        current_size = 1
        while True:
            current_mod = current % K
            if current_mod == 0:
                return current_size
            if current_mod in seen_mod:
                return -1
            seen_mod.add(current_mod)
            current = current * 10 + 1
            current_size += 1
