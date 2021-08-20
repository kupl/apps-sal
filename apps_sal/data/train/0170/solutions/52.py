class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if arr == list(sorted(arr)):
            return 0
        increasing_parts = []
        curr = []
        for num in arr:
            if not curr or curr[-1] <= num:
                curr.append(num)
            else:
                increasing_parts.append(curr)
                curr = [num]
        increasing_parts.append(curr)
        first = set(increasing_parts[0])
        second = set(increasing_parts[-1])
        first_pos = {}
        sec_pos = {}
        last_start = sum([len(x) for x in increasing_parts[:-1]])
        for (i, num) in enumerate(increasing_parts[0]):
            first_pos[num] = i
        for (i, num) in enumerate(increasing_parts[-1]):
            sec_pos[num] = i + last_start
        best = 0
        seq = list(sorted(increasing_parts[0] + increasing_parts[-1]))
        for (i, num) in enumerate(seq):
            if num in first:
                if i < len(seq) - 1 and seq[i + 1] in second:
                    best = max(first_pos[num] + 1 + len(arr) - sec_pos[seq[i + 1]], best)
        return min([len(arr) - len(increasing_parts[0]), len(arr) - len(increasing_parts[-1]), len(arr) - best])
