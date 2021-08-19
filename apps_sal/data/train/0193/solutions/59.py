class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        occ = {}
        for num in arr:
            if num in occ:
                occ[num] += 1
            else:
                occ[num] = 1
        occ_lst = list(occ.items())
        occ_lst.sort(key=lambda x: x[1], reverse=True)
        total_elems_removed = 0
        removal_set_size = 0
        for (i, (_, num_occur)) in enumerate(occ_lst):
            total_elems_removed += num_occur
            if total_elems_removed >= math.ceil(len(arr) / 2.0):
                return i + 1
