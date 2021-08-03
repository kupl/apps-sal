class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)

        fullsum = sum(nums)

        toremove = fullsum % p
        d = defaultdict(int)
        d[0] = -1
        cumsum = 0
        answer = n
        for index, number in enumerate(nums):
            cumsum += number
            cumsum = cumsum % p
            d[cumsum] = index
            if (cumsum - toremove) % p in d:
                answer = min(answer, index - d[(cumsum - toremove) % p])

        if answer < n:
            return answer
        else:
            return -1
