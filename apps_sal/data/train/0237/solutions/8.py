class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        container = [0]
        for num in A:
            container.append(container[-1] + num)

        count = Counter()

        ans = 0
        for num in container:
            ans += count[num]
            count[num + S] += 1

        return ans
