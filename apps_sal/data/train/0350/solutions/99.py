class Solution:

    def _identify_limit(self, A, current_limit, K, char_count_after_limit):
        char_count_after_limit = {k: v for k, v in char_count_after_limit.items()}
        unique_chars = {i for i in char_count_after_limit if char_count_after_limit[i] > 0}
        while len(unique_chars) == K:
            temp_char = A[current_limit]
            char_count_after_limit[temp_char] = char_count_after_limit[temp_char] - 1
            if char_count_after_limit[temp_char] == 0:
                unique_chars.remove(temp_char)
            current_limit += 1

        char_count_after_limit[A[current_limit - 1]] = char_count_after_limit[A[current_limit - 1]] + 1
        return current_limit - 1, char_count_after_limit

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        counter1, counter2 = collections.Counter(), collections.Counter()
        slow = fast = res = 0

        for _, a in enumerate(A):
            counter1[a], counter2[a] = counter1[a] + 1, counter2[a] + 1
            while len(counter2) == K:
                counter2[A[fast]] -= 1
                if not counter2[A[fast]]:
                    del counter2[A[fast]]
                fast += 1
            while len(counter1) > K:
                counter1[A[slow]] -= 1
                if not counter1[A[slow]]:
                    del counter1[A[slow]]
                slow += 1
            res += fast - slow

        return res
