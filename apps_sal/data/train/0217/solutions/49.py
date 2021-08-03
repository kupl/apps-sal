class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        arr_len = len(A)
        final_result_set = set()
        pre_result_set = set()
        pre_result_set.add(A[0])
        final_result_set.add(A[0])
        for i in range(1, arr_len):
            cur_result_set = set()
            for pre_result in pre_result_set:
                one_cur_result = pre_result | A[i]
                cur_result_set.add(one_cur_result)
                final_result_set.add(one_cur_result)
            cur_result_set.add(A[i])
            final_result_set.add(A[i])
            pre_result_set = cur_result_set
        return len(final_result_set)
