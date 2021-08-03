class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        N = len(arr)
        prefix = [N + 1] * N
        suffix = [N + 1] * N

        presum = dict()
        total = 0
        presum[0] = -1
        for i in range(N):
            total += arr[i]
            presum[total] = i

        prefix[0] = N + 1
        total = 0
        for i in range(0, N):
            total += arr[i]
            t = N + 1
            xx = total - target
            if xx in presum:
                #   找到一个target
                t = i - presum[xx]
            prefix[i] = min(prefix[i - 1], t)

        sufsum = dict()
        total = 0
        sufsum[0] = N
        for i in range(N - 1, -1, -1):
            total += arr[i]
            sufsum[total] = i

        total = 0
        if arr[-1] == target:
            suffix[-1] = 1
        total = arr[-1]
        for i in range(N - 2, -1, -1):
            total += arr[i]
            t = N + 1
            xx = total - target
            if xx in sufsum:
                #   找到一个target
                t = sufsum[xx] - i
            suffix[i] = min(suffix[i + 1], t)

        # print(prefix)
        # print(suffix)

        rtv = N + 1
        for i in range(N - 1):
            cur = prefix[i] + suffix[i + 1]
            rtv = min(rtv, cur)
        if rtv > N:
            return -1
        return rtv
