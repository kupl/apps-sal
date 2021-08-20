class Solution:

    def minJumps(self, arr: List[int]) -> int:
        c = collections.defaultdict(list)
        for (i, x) in enumerate(arr):
            c[x].append(i)
        q = [0]
        steps = [0] * len(arr)
        steps[0] = 1
        seen = set()
        while q:
            i = q.pop(0)
            if i == len(arr) - 1:
                return steps[i] - 1
            children = [i - 1, i + 1]
            if arr[i] not in seen:
                children += c[arr[i]][::-1]
                seen.add(arr[i])
            for child in children:
                if child < 0 or child >= len(arr):
                    continue
                if child == i:
                    continue
                if steps[child]:
                    continue
                steps[child] = steps[i] + 1
                q.append(child)
        return steps[-1] - 1
