class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def at_most_k(arr, k):
            start = 0
            counter = Counter()
            uniques = 0
            res = 0
            for i in range(len(A)):
                counter[A[i]] += 1
                if counter[A[i]] == 1:
                    uniques += 1

                while uniques > k:
                    counter[A[start]] -= 1
                    if counter[A[start]] == 0:
                        uniques -= 1

                    start += 1

                res += i - start

            return res

        return at_most_k(A, K) - at_most_k(A, K - 1)
