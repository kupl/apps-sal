class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        int_dict = {}
        int_sorted_list = []
        current = 0
        l = len(A)
        count = 0
        while current < l:
            if int_dict.get(A[current]) != None:
                int_sorted_list.remove(A[current])
            int_dict[A[current]] = current
            int_sorted_list.append(A[current])
            if len(int_sorted_list) > K + 1:
                del int_dict[int_sorted_list[0]]
                del int_sorted_list[0]
            if len(int_sorted_list) > K:
                count += int_dict[int_sorted_list[-K]] - int_dict[int_sorted_list[-K - 1]]
            elif len(int_sorted_list) == K:
                count += int_dict[int_sorted_list[-K]] + 1
            current += 1
        return count
