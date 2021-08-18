class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        cache = {}

        def sim(n, count, curr_element):
            if curr_element:
                if count > rollMax[curr_element - 1]:
                    return float('inf')

            if (n, count, curr_element) in cache:
                return cache[(n, count, curr_element)]

            if n == 0:
                return 1

            all_ans = 0
            for i in range(1, 7):
                if curr_element == i:
                    ans = sim(n - 1, count + 1, i)
                else:
                    ans = sim(n - 1, 1, i)

                if ans != float('inf'):
                    all_ans += ans

            cache[(n, count, curr_element)] = all_ans
            return all_ans

        return sim(n, 0, 0) % 1000000007
