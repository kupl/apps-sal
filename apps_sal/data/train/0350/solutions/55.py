class Solution:
    
    def _identify_limit(self, A, current_limit, K,  char_count_after_limit):
        # unique_chars = {i for i in char_count_after_limit if char_count_after_limit[i] > 0}
        # print(unique_chars)
        temp_char = A[current_limit]
        while char_count_after_limit.get(temp_char, 0) > 1 : 
            # print(\"WHILE\", char_count_after_limit)
            char_count_after_limit[temp_char] = char_count_after_limit[temp_char] - 1
            current_limit += 1
            temp_char = A[current_limit]
            

        return  current_limit , char_count_after_limit
    
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        char_info = {item : [] for item in set(A)} 
        unique_char_count = {}
        unique_char = set()
        start_idx = 0 
        end_idx = 0
        num_substr = 0
        current_subarray = []
        current_valid_count = 0 
        # In any valid subarray what is the index upto which left index could be moved without making subarray bad 
        # Whenever end_idx is moved to right keeping subarray good compute limit_idx again 
        limit_idx = 0
        while end_idx < len(A) + 1 : 
            if len(unique_char_count) == K : 
                limit_idx, unique_char_count = self._identify_limit(A, limit_idx, K, unique_char_count)
                num_substr += limit_idx - start_idx + 1
                if end_idx < len(A):
                    current_char = A[end_idx]
                    unique_char_count[current_char] = unique_char_count.get(current_char, 0) + 1
                end_idx += 1 
            elif len(unique_char_count) > K: 
                # Remove limit_idx from stats
                current_char = A[limit_idx]
                unique_char_count.pop(current_char)
                start_idx = limit_idx + 1
                limit_idx = start_idx 
            else: 
                if end_idx < len(A):
                    current_char = A[end_idx]
                    unique_char_count[current_char] = unique_char_count.get(current_char, 0) + 1
                end_idx += 1 
        return num_substr

    
    
    #         counter1, counter2 = collections.Counter(), collections.Counter()
#         slow = fast = res = 0

#         for _, a in enumerate(A):
#             counter1[a], counter2[a] = counter1[a] + 1, counter2[a] + 1
#             while len(counter2) == K:
#                 counter2[A[fast]] -= 1
#                 if not counter2[A[fast]]: del counter2[A[fast]]
#                 fast += 1
#             while len(counter1) > K:
#                 counter1[A[slow]] -= 1
#                 if not counter1[A[slow]]: del counter1[A[slow]]
#                 slow += 1
#             res += fast - slow

#         return res

