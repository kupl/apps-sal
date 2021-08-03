class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        counter1, counter2 = collections.Counter(), collections.Counter()
        slow = fast = res = 0

        for a in A:
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
