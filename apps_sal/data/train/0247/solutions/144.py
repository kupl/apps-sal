class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        def getPrefix(arr):
            m = {0: -1}
            prefix = [float('inf')]
            s = 0
            for i, n in enumerate(arr):
                s += n
                minn = prefix[-1]
                if (s - target) in m:
                    minn = min(i - m[s - target], minn)
                prefix.append(minn)
                m[s] = i
            prefix.pop(0)
            return prefix

        prefix = getPrefix(arr)
        sufix = list(reversed(getPrefix(reversed(arr))))
        ans = float('inf')
        for i in range(len(arr) - 1):
            ans = min(ans, prefix[i] + sufix[i + 1])
        return ans if ans != float('inf') else -1
