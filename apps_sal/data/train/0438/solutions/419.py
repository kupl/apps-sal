class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        parent = [i for i in range(len(arr))]

        def union(a, b):
            par_a = find(a)
            par_b = find(b)
            if par_a == par_b:
                return
            if par_a > par_b:
                par = par_a
            else:
                par = par_b
            parent[par_a] = par
            parent[par_b] = par

        def find(a):
            if parent[a] == a:
                return a
            else:
                parent[a] = find(parent[a])
                return parent[a]
        ans = -1
        contigAtI = [0] * len(arr)
        counts = [0] * (len(arr) + 1)
        s = [0] * len(arr)
        for (idx, item) in enumerate(arr):
            s[item - 1] = 1
            contigAtI[item - 1] = 1
            counts[contigAtI[item - 1]] += 1
            if item - 2 >= 0 and s[item - 2] == 1:
                counts[contigAtI[item - 2]] -= 1
                counts[contigAtI[item - 1]] -= 1
                contigAtI[item - 1] += contigAtI[item - 2]
                counts[contigAtI[item - 1]] += 1
                union(item - 2, item - 1)
            if item < len(arr) and s[item] == 1:
                endPtr = find(item)
                counts[contigAtI[item - 1]] -= 1
                counts[contigAtI[endPtr]] -= 1
                contigAtI[endPtr] += contigAtI[item - 1]
                counts[contigAtI[endPtr]] += 1
                union(item - 1, endPtr)
            if counts[m] > 0:
                ans = max(ans, idx + 1)
        return ans
