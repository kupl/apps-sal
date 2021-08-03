class Solution:
    def maxLength(self, arr: List[str]) -> int:
        if len(arr) == 1:
            if len(set(arr[0])) == len(list(arr[0])):
                return len(set(arr[0]))
            else:
                return 0

        all_combinations = []
        max_ = 0
        for r in range(1, len(arr) + 1):
            combinations_object = itertools.combinations(arr, r)
            combinations_list = list(combinations_object)
            for st in combinations_list:
                comb = ''.join(st)
                if len(set(comb)) == len(comb):
                    max_ = max(max_, len(comb))

        return max_
