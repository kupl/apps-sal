class Solution:

    def minJumps(self, arr: List[int]) -> int:
        record = {}
        for (idx, item) in enumerate(arr, 0):
            if item not in record:
                record[item] = [idx]
            elif record[item][-1] + 2 >= idx:
                record[item][-1] = idx
            else:
                record[item].append(idx)
        queue = [0]
        ret = [-1] * len(arr)
        ret[0] = 0
        step = 0
        last = len(arr) - 1
        while queue:
            target = []
            step += 1
            for idx in queue:
                if idx > 0 and ret[idx - 1] == -1:
                    target.append(idx - 1)
                    ret[idx - 1] = step
                if idx + 1 < len(arr) and ret[idx + 1] == -1:
                    target.append(idx + 1)
                    ret[idx + 1] = step
                    if idx + 1 == last:
                        return step
                for pos in record[arr[idx]]:
                    if pos == idx:
                        continue
                    if ret[pos] == -1:
                        target.append(pos)
                        ret[pos] = step
                        if pos == last:
                            return step
            queue = target
        return ret[-1]
