class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        total_sum = sum(A)
        sum_dict = collections.defaultdict(set)

        for val in A:
            temp_list = [(1, val)]
            for key, set_val in sorted(sum_dict.items()):
                if key == len(A) // 2:
                    break
                for sum_val in set_val:
                    temp_list.append((key + 1, val + sum_val))
            for key_val, sum_val in temp_list:
                sum_dict[key_val].add(sum_val)

        for i in range(len(A) - 1):
            if (total_sum * (i + 1) / len(A)) in sum_dict[i + 1]:
                return True
        return False
