class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        seen = set()
        heads = set()
        tails = set()
        forward = dict()
        reverse = dict()

        for n in nums:

            if n in seen:
                continue
            else:
                seen.add(n)

            if n - 1 not in tails and n + 1 not in heads:
                heads.add(n)
                tails.add(n)
                forward[n] = n
                reverse[n] = n

            if n - 1 not in tails and n + 1 in heads:
                heads.remove(n + 1)
                heads.add(n)
                tail = forward[n + 1]
                del forward[n + 1]
                forward[n] = tail
                reverse[tail] = n

            if n - 1 in tails and n + 1 not in heads:
                tails.remove(n - 1)
                tails.add(n)
                head = reverse[n - 1]
                del reverse[n - 1]
                reverse[n] = head
                forward[head] = n

            if n - 1 in tails and n + 1 in heads:
                head = reverse[n - 1]
                tail = forward[n + 1]
                heads.remove(n + 1)
                tails.remove(n - 1)
                del forward[n + 1]
                del reverse[n - 1]
                forward[head] = tail
                reverse[tail] = head

        diffs = [v - k + 1 for (k, v) in list(forward.items())]
        maxRun = max(diffs)

        return maxRun
