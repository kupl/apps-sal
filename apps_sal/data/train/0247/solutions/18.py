class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        #    h[key] stores list of indices, let ind = h[key][-1] 
        #    Here, run[ind] == key (INCLUDING arr[ind - 1]) 
        run = [0, arr[0]]
        h = {0: 0, arr[0]: 1}
        prefix = [len(arr)] 
        for i in range(1, len(arr)):
            if run[i] - target in h:
                prefix.append(min(prefix[-1], i - h[run[i] - target]))
            else:
                prefix.append(prefix[-1])
            run.append(run[-1] + arr[i])
            h[run[-1]] = i + 1
        suffix = [len(arr) for i in range(len(arr))]
        if arr[-1] == target:
            suffix[-1] = 1
        for i in range(len(arr) - 2, -1, -1):
            if run[i] + target in h:
                suffix[i] = min(suffix[i + 1], h[run[i] + target] - i)
            else:
                suffix[i] = suffix[i + 1]
        res = len(arr) + 1
        for i in range(len(arr)):
            if not (prefix[i] == len(arr) or suffix[i] == len(arr)):
                res = min(res, prefix[i] + suffix[i])
        if res == len(arr) + 1:
            return -1
        return res
