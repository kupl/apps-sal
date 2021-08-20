class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m

        def find(vals, index):
            if vals[index] != -1:
                vals[index] = find(vals, vals[index])
                return vals[index]
            else:
                return index

        def unionStart(a, b):
            root_a = find(start, a)
            root_b = find(start, b)
            if root_a < root_b:
                start[root_b] = root_a
            else:
                start[root_a] = root_b

        def unionEnd(a, b):
            root_a = find(end, a)
            root_b = find(end, b)
            if root_a > root_b:
                end[root_b] = root_a
            else:
                end[root_a] = root_b

        def getLength(index):
            start_curr = find(start, index)
            end_curr = find(end, index)
            return end_curr - start_curr + 1
        res = -1
        nums = [0 for i in range(len(arr))]
        start = [-1 for i in range(len(arr))]
        end = [-1 for i in range(len(arr))]
        mem = dict()
        lengths = collections.Counter()
        for i in range(len(arr)):
            index = arr[i] - 1
            nums[index] += 1
            if index > 0 and nums[index - 1] == 1:
                old_length = getLength(index - 1)
                lengths[old_length] -= 1
                unionStart(index - 1, index)
                unionEnd(index - 1, index)
            if index < len(arr) - 1 and nums[index + 1] == 1:
                old_length = getLength(index + 1)
                lengths[old_length] -= 1
                unionStart(index, index + 1)
                unionEnd(index, index + 1)
            start_curr = find(start, index)
            end_curr = find(end, index)
            length = getLength(index)
            lengths[length] += 1
            if lengths[m] > 0:
                res = i + 1
        return res
