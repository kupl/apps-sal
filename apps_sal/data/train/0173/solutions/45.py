class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        if len(arr) % 2 != 0:
            raise Exception('Input array is of odd size!')
        mod_dict = {}
        for i in arr:
            mod = i % k
            pair_mod = (k - mod) % k
            if pair_mod in mod_dict:
                if mod_dict[pair_mod] == 1:
                    del mod_dict[pair_mod]
                else:
                    mod_dict[pair_mod] -= 1
            elif mod not in mod_dict:
                mod_dict[mod] = 1
            else:
                mod_dict[mod] += 1
        return len(mod_dict) == 0
