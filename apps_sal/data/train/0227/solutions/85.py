class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        hash_count = dict()
        hash_count[1] = 0
        start = 0
        max_count = 0
        max_result = 0
        for end in range(len(A)):
            if A[end] == 1:
                hash_count[A[end]] += 1
            max_count = max(max_count, hash_count[1])
            # print(f\" {max_count + K}  comp  {end - start + 1}\")
            if max_count + K < (end - start + 1):
                if A[start] == 1 and hash_count.get(1):
                    hash_count[1] -= 1
                start += 1
            max_result = max(max_result, end - start + 1)
            # print(max_result)
        return max_result
