class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        counter = collections.Counter()
        hs = {}
        n = len(arr)

        def find(x, union):
            root = x
            if union[x] != x:
                union[x] = find(union[x], union)
            return union[x]
        union = {}
        res = -1
        for i in range(n):
            idx = arr[i]
            union[idx] = idx
            hs[idx] = 1
            counter[1] += 1
            if idx - 1 in union:
                left = find(idx - 1, union)
                union[idx] = find(idx - 1, union)
                counter[hs[left]] -= 1
                counter[hs[idx]] -= 1
                counter[hs[left] + hs[idx]] += 1
                hs[left] += hs[idx]
            if idx + 1 in union:
                right = find(idx + 1, union)
                union[idx + 1] = find(idx, union)
                t = find(idx, union)
                counter[hs[right]] -= 1
                counter[hs[t]] -= 1
                counter[hs[right] + hs[t]] += 1
                hs[t] += hs[right]
            if counter[m] > 0:
                res = i + 1
        return res
